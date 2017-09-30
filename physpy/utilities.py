def diff(theor, real):
    print('diff epsilon = {:.2f}%'.format(abs(theor - real) / theor * 100))
