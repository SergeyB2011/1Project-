import  requests
counter_key = 0
res_parse_list = {}
response = requests.get("https://meteo.ua/34/kiev#2023-09-02--18-00")#https://bank.gov.ua/
response_text = response.text
response_parse = response_text.split("<div class->")#<div class="value">
for parse_element_1 in response_parse:
    if(parse_element_1.startswith(">9:00<")):
        sequence = parse_element_1.split("</div>")
        for parse_element_2 in sequence:
                if parse_element_2.startswith(">9:00<") and parse_element_2[1].isdigit():
                    res_parse_list[counter_key] = parse_element_2
                    counter_key += 1
print(res_parse_list)