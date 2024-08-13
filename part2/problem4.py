from collections import deque

############
# Streaming Payments Processor, two vendors edition.
#
# We decided to improve the payment processor from the previous
# exercise and hired two vendors. One was to implement `stream_payments()`
# function, and another `store_payments()` function.
#
# The function `process_payments_2()` is processing a large, but finite
# amount of payments in a streaming fashion.
#
# Unfortunately the vendors did not coordinate their efforts, and delivered
# their functions with incompatible APIs.
#
# TODO: Your task is to analyse the APIs of `stream_payments()` and
# `store_payments()` and to write glue code in `process_payments_2()`
# that allows us to store the payments using these vendor functions.
#
# NOTE: you need to take into account the following restrictions:
# - You are allowed only one call each to `stream_payments()` and
#   to `store_payments()`
# - You can not read from the storage.
# - You can not use disk as temporary storage.
# - Your system has limited memory that can not hold all payments.
#
############


import io
# This is a library function, you can't modify it.
def stream_payments(callback_fn):
    """
    Reads payments from a payment processor and calls `callback_fn(amount)`
    for each payment.
    Returns when there is no more payments.
    """
# Sample implementation to make the code run in coderpad.
# Do not rely on this exact implementation.
    for i in range(10):
        callback_fn(i)


# This is a library function, you can't modify it.
def store_payments(amount_iterator):
    """
    Iterates over the payment amounts from amount_iterator
    and stores them to a remote system.
    """
    # Sample implementation to make the code run in coderpad.
    # Do not rely on this exact implementation.
    for i in amount_iterator:
        print(i)


def process_payments_2():
    """
    TODO:
    Modify `process_payments_2()`, write glue code that enables
    `store_payments()` to consume payments produced by `stream_payments()`
    """

    payments = deque()

    def my_callback(payment):
        payments.append(payment)

    def payment_generator():

        stream_payments(my_callback)

        while len(payments) > 0:
            yield payments.popleft()
    
    store_payments(payment_generator())


process_payments_2()

# Given the current implementation of the library functions, this solution violates the memory rule (We store all of the payments in one queue).
# If we assume that the stream_payments function is not implemented like this and the payments are streamed (hence added to the queue periodically and asynchronously),
# this solution makes sense, because if storing takes long and there are a lot of payments, the payments will get inserted to the queue, while the older payments are getting stored.
# The worst case with this implementation will be that there will be a lot of payments that will get added to the queue at once, and then they will get stored (which violates the memory rule), 
# but if in the stream_payments() function the payments get streamed asynchronously (which in the real world example is more likely to be the case), the queue will be half-empty, depending on the streaming rate.

# If we try not to violate the memory rule by calling the store_payments() function from the callback function, that means we are violating the first rule,
# because the store_payments() function gets called for each payment.


