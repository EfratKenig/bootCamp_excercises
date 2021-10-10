import threading

db = {
    "result": []
}


def all_primes(lower, upper):
    for num in range(lower, upper + 1):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            threadLock.acquire()
            db["results"].append(num)
            threadLock.release()
    return


def main(m, n):
    number = m
    part_size = int(number / n)
    if part_size != number / n:
        one_more = True
    threads = []
    # each thread will be sent to calc() to calculate a range of numbers.
    if not one_more:
        # each thread calculates range of m/n different numbers
        for i in range(n):
            lower = number - m / n
            upper = number
            number -= m / n
            t = threading.Thread(target=all_primes, args=[lower, upper])
            threads.append(t)
            t.start()
    else:
        # n-1 threads calculate range of int(m/n-1) different numbers and the last thread calculates the remainder
        first_part = int(m/n-1)
        for i in range(n):
            lower = number - first_part
            upper = number
            number -= first_part
            t = threading.Thread(target=all_primes, args=[lower, upper])
            threads.append(t)
            t.start()
    for t in threads:
        t.join()
    print(db["results"])


if __name__ == "__main__":
    threadLock = threading.Lock()
    m = 50
    n = 10
    main(m, n)

# Question 1
# Write a program whose job is to calculate in parallel the series
# of prime numbers between 1 and m. The program will get as parameters
# two positive integers m and n. m represents the number up to it you
# must find the prime numbers, and n is the number of threads that can
# be run simultaneously. The program will check all the numbers in the
# range of 1…m and print the prime numbers in order.
# The numbers will be checked as follows:
# Each thread will refer to a database of numbers to get one
# to be checked. The threads will simultaneously check the number
# they received and at the end they will contact the database to
# update the answer. The thread will repeat the operations as long
# as there are numbers in the database to check. The thread will end
# when there are no more numbers in the database.
# Instruction:
# The program includes the following elements:
# - A database of numbers responsible for the division of labor and the preservation of results.
# - n threads.
# - You must make sure that all the processes finish their job before printing the results.
# - The program must check the correctness of the parameters.
# Use the program you wrote to print the prime numbers from
# 1 to 1000, using ten processes that test in parallel
