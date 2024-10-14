# from src.customer import *
from src.inventory import *
from src.sales import *
from hashlib import md5

auth = pd.read_csv("data/auth.csv")
hash_list = []
for user_hashes in auth["user_name"]:
    hash_list.append(user_hashes)


class Auth:
    def createUser(user_name, password):

        with open("data/auth.csv", "a") as Auth:
            Auth.write(
                "\n{},{}".format(
                    md5(str(user_name).encode("UTF-8")).hexdigest(),
                    md5(str(password).encode("UTF-8")).hexdigest(),
                )
            )

    def authenticate(user_name, password):
        if md5(str(user_name).encode("utf-8")).hexdigest() in hash_list:
            if (
                md5(str(password).encode("utf-8")).hexdigest()
                == auth["password"][hash_list.index(md5(str(user_name).encode("utf-8")).hexdigest())]
            ):
                print("authentication successfull")
                return True
        else:
            return False
