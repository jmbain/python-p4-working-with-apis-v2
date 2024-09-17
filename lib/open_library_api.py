import requests
import json


class Search:

    def get_search_results(self):
        search_term = "the lord of the rings"

        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        # formats the list into a comma separated string
        # output: "title,author_name"
        fields_formatted = ",".join(fields)
        limit = 1

        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"

        response = requests.get(URL)
        return response.content

    def get_search_results_json(self):
        search_term = "the lord of the rings" #sets default search term

        search_term_formatted = search_term.replace(" ", "+") #format search term to remove blank spaces, important for URL bar
        fields = ["title", "author_name"] # generate fields list
        fields_formatted = ",".join(fields) #join fields list into a csv string
        limit = 1 # determines limit of how many items pulled from get request

        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}" #dynamic url for get request using search term user input and fstring
        print(URL) #print for backend review
        response = requests.get(URL) #store request data in variable for later use
        return response.json() #return JSON-ified version of requested data variable

    def get_user_search_results(self, search_term):
        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"

        response = requests.get(URL).json()
        response_formatted = f"Title: {response['docs'][0]['title']}\nAuthor: {response['docs'][0]['author_name'][0]}"
        return response_formatted


# results = Search().get_search_results()
# print(results)

# results_json = Search().get_search_results_json()
# print(json.dumps(results_json, indent=1))

search_term = input("Enter a book title: ") #Gather user input, search_term variable used in multiple methods...
result = Search().get_user_search_results(search_term) #Store search class method result for search_term into result variable
print("Search Result:\n")
print(result)
