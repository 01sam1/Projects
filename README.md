# Projects
### Description
> This is a project related to parsing students result from the board website and store the result in .csv file.
> i have wrote a program such a way that take one valid board seat number and store 50 sequential seat no.'s data in csv file.
## Programming language
> python 3....
### requirements
- requests
- beautiful-soup
- csv module
### 📌list of functions
- inputs(data ,total_seat_digit) -> this function takes seat no as a data and total_seat_digit is use for validation of seat number.
- parse2(ele) ->takes parsed data, contains list of elements (in this case list of <td> elements)
- parse_web(content) -> content is html content return from requests.data. the function takes html content and parse the content using beautiful-soup.
the function call parse2 named function.
- data_arrange(data:list) -> simple fuction to resuffles the elements of list. this function makes name data and seat no data at first position.
- requests(url,headers,seat_no) -> ``**core function of the project.** __url and headers have default values.__ ``by simply providing seat no. the function retunrs the result data for the given seat no. in appropriate format. ``this func compile all above fucntion.``
- main() ->flexible function for individul users.

### ⚙️ Improvable (Features that are implementable)
- can be use threading module for Concurrency. <br>
- can create a flow that takes file of lists of seat numbers and store the result data in csv file.<br>
- for one invalid seat no program control shouldn't be terminate.<br>
- can be create proper structure of try-catch conditions.<br>
