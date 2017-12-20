from libs import urlloader
from urllib.error import HTTPError
import json

class Swapi:

    base_url = 'https://swapi.co/api/'
    __people = None

    def __get_result(self,resource):
        try:
            api_result = urlloader.load_url(self.base_url + resource)
            result_json = json.loads(api_result)
            return result_json['results']
        except HTTPError as error:
            print("Erorr al cargar url: ",repr(error))
            return None
        except Exception as ex:
            print("Erorr al cargar url: ",repr(error))
            return None

    def get_people(self):
        if self.__people:
            return self.__people

        result = self.__get_result('people/')
        self._people = [(person['name'],person['gender'])for person in result]
        return self._people


s = Swapi()
s.get_people()