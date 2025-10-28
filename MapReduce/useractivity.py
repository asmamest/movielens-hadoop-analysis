from mrjob.job import MRJob

class UserActivity(MRJob):

    def mapper(self, _, line):
        user_id, movie_id, rating, timestamp = line.split('\t')
        yield user_id, 1

    def reducer(self, user_id, counts):
        yield user_id, sum(counts)

if __name__ == '__main__':
    UserActivity.run()
