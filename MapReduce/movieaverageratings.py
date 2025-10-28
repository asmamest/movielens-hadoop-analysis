from mrjob.job import MRJob
from mrjob.step import MRStep

class MovieAverageRatings(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings,
                   reducer=self.reducer_count_ratings),
            MRStep(reducer=self.reducer_find_avg)
        ]

    def mapper_get_ratings(self, _, line):
        user_id, movie_id, rating, timestamp = line.split('\t')
        yield movie_id, float(rating)

    def reducer_count_ratings(self, movie_id, ratings):
        total = count = 0
        for rating in ratings:
            total += rating
            count += 1
        yield movie_id, (total, count)

    def reducer_find_avg(self, movie_id, totals_counts):
        for total, count in totals_counts:
            yield movie_id, total / count

if __name__ == '__main__':
    MovieAverageRatings.run()
