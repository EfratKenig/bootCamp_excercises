import re
import random
import string


# -------------------------
# first part:
def validate_password(psd=None):
    if psd is None:
        psd = input("psd: ")
    try:
        assert 7 < len(psd) < 21 and \
               re.search('\d', psd) and \
               re.search('[$#!%@]', psd) and \
               len(re.findall('[a-z]', psd)) > 3 and \
               len(re.findall('[A-Z]', psd)) > 1, "False"
        return True
    except AssertionError as err:
        return err


# -------------------------
# second part:
def generate_psd():
    ints_length = random.randrange(1, 4)
    lowers_length = random.randrange(4, 7)
    uppers_length = random.randrange(2, 5)
    specials_length = random.randrange(1, 3)

    ints = [str(random.randrange(0, 10)) for _ in range(ints_length)]
    lowers = [random.choice(string.ascii_lowercase) for _ in range(lowers_length)]
    uppers = [random.choice(string.ascii_uppercase) for _ in range(uppers_length)]
    specials = [random.choice(['$', '#', '!', '%', '@']) for _ in range(specials_length)]
    n = ints + lowers + uppers + specials
    random.shuffle(n)
    new_psd = ''.join(n)
    return new_psd
