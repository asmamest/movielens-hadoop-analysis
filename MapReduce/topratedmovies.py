from mrjob.job import MRJob
from mrjob.step import MRStep

class TopRatedMovies(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings,
                   reducer=self.reducer_calculate_average),
            MRStep(mapper=self.mapper_sort_movies,
                   reducer=self.reducer_output_top)
        ]

    def mapper_get_ratings(self, _, line):
        user_id, movie_id, rating, timestamp = line.split('\t')
        yield movie_id, float(rating)

    def reducer_calculate_average(self, movie_id, ratings):
        total_rating = count = 0
        for rating in ratings:
            total_rating += rating
            count += 1
        average_rating = total_rating / count
        yield None, (average_rating, movie_id)

    def mapper_sort_movies(self, _, movie_data):
        # Emit average_rating as key to sort
        average_rating, movie_id = movie_data
        yield '%.3f' % average_rating, movie_id


    def reducer_output_top(self, average_rating, movie_ids):
        for movie_id in movie_ids:
            yield average_rating, movie_id

if __name__ == '__main__':
    TopRatedMovies.run()
