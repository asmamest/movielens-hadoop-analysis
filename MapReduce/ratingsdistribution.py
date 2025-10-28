from mrjob.job import MRJob

class RatingsDistribution(MRJob):

    def mapper(self, _, line):
        user_id, movie_id, rating, timestamp = line.split('\t')
        yield rating, 1

    def reducer(self, rating, counts):
        yield rating, sum(counts)

if __name__ == '__main__':
    RatingsDistribution.run()
