import random
import re
import requests
import bs4
from requests_html import HTMLSession
import time
from http import HTTPStatus

class GForms:
    entries_id_and_question_dict = {}

    def __init__(self, form_url, verbose=False) -> None:
        self.__form_url = form_url
        self.__verbose = verbose

    def set_verbose(self, verbose):
        self.__verbose = verbose

    def __get_entries_id_and_question_dict(self):
        # get the page content of the formLink
        if (self.__verbose):
            print(f"Getting the page content of {self.__form_url}...")
            
        t1 = time.time()
        session = HTMLSession()
        r = session.get(self.form_url)
        r.html.render(sleep=.1, keep_page=True)

        if (self.__verbose):
            print("Got the page content of the formLink in {:.2f} seconds".format(time.time() - t1))

        if (self.__verbose):
            print("Extracting the data...")
            
        t1 = time.time()
        soup = bs4.BeautifulSoup(r.html.html, "html.parser")

        # get the question from the data-params value of html elements with jsmodel attribute
        entries_data_params = [entry["data-params"] for entry in soup.select("[jsmodel]") if "data-params" in entry.attrs]

        
        for data_params in entries_data_params:
            if len(data_params.split("[[")) > 2: # means that it is a multiple choice question
                self.entries_id_and_question_dict[data_params.split('"')[1]] = [None, None]

                mcq = [response.split('"')[1] for response in data_params.split("[[")[2].split("]]")[0].split("],[")]

                self.entries_id_and_question_dict[data_params.split('"')[1]][0] = "entry." + data_params.split("[[")[1].split(",")[0] + "_sentinel"
                self.entries_id_and_question_dict[data_params.split('"')[1]][1] = mcq
            else:
                self.entries_id_and_question_dict[data_params.split('"')[1]] = "entry." + data_params.split("[[")[1].split(",")[0]

        def get_number_of_questions():
            return len(self.entries_id_and_question_dict)
        
        def get_question(index):
            # returns the question at the given index
            return list(self.entries_id_and_question_dict.keys())[index]