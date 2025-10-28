from mrjob.job import MRJob
import time

class RatingTrends(MRJob):

    def mapper(self, _, line):
        user_id, movie_id, rating, timestamp = line.split('\t')
        year = time.strftime('%Y', time.gmtime(int(timestamp)))
        yield year, 1

    def reducer(self, year, counts):
        yield year, sum(counts)

if __name__ == '__main__':
    RatingTrends.run()
