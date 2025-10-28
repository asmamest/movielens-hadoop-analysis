from mrjob.job import MRJob

class MoviePopularity(MRJob):

    def mapper(self, _, line):
        # Splitting each line by tab
        user_id, movie_id, rating, timestamp = line.split('\t')
        yield movie_id, 1

    def reducer(self, movie_id, counts):
        yield movie_id, sum(counts)

if __name__ == '__main__':
    MoviePopularity.run()
