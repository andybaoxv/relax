from __future__ import absolute_import
from __future__ import print_function
import matplotlib.pyplot as plt

import numpy as np
import numpy.random as npr
from scipy.special import expit, logit


def logistic_sample(mu, sigma, noise):
    return mu + logit(noise) * sigma

def logistic_logpdf(x, mu=0, scale=1):
    y = (x - mu) / (2 * scale)
    return -2 * np.logaddexp(y, -y) - np.log(scale)

if __name__ == '__main__':

    rs = npr.RandomState(0)
    num_samples = 50000

    mu = 2.3
    sigma = 0.8

    # Set up figure.
    fig = plt.figure(figsize=(8, 8), facecolor='white')

    samples = logistic_sample(mu, sigma, rs.rand(num_samples))

    plt.hist(samples, bins=1000)

    x = np.linspace(-10, 10, 1000)
    y = 900*np.exp(logistic_logpdf(x, mu, sigma))

    plt.plot(x, y)
    plt.xlim([-10,10])
    plt.pause(10.0)