import logging
import re


def parse_single_string(cond, table_subquery_name_pair):
    logger = logging.getLogger("neuron.util.parse_single_string")
    logger.debug(cond)
    # remove parentheses
    # if cond[0] == '(' and cond[-1] == ')':
    #    parsed_cond = cond[1:-1]
    # else:
    #    parsed_cond = cond

    # replace syntax with natural language
    parsed_cond = re.sub(r"::\"?[a-zA-Z\s]+\"?", "", cond)
    parsed_cond = parsed_cond.replace("<>", "not equals") \
                             .replace("count(*)", "count(all)") \
                             .replace("DESC", "in a descending order") \
                             .replace("ASC", "in a ascending order")
    logger.debug(parsed_cond)
    # .replace("::text", "")
    # .replace("::char", "")
    if "NOT" in parsed_cond:
        parsed_cond = parsed_cond.replace("NOT", "records not in")
    if "regexp" in parsed_cond:
        parsed_cond = re.search(r'\(.*\)', parsed_cond).group(0).split(",")[0][1:] + " processed by " + parsed_cond
    if "~~" in parsed_cond:
        regexp = re.search(r"~~\*? '.+'", parsed_cond)
        substring = regexp.group(0)[re.search(r"'.+'", regexp.group(0)).start():]  # substring is the search condition in SQL

        number_of_percentage_sign = substring.count("%")
        # if starting or ending with
        if number_of_percentage_sign == 1 and (substring[1] == "%" or substring[-2] == "%"):
            if substring[1] == '%':
                replacement = " ended with " + substring.replace("%", "")
            if substring[-2] == '%':
                replacement = " started with " + substring.replace("%", "")
        elif number_of_percentage_sign > 1:
            keywords = substring.replace("'", "").strip("%").split("%")
            keywords = ["'" + word + "'" for word in keywords]
            replacement = " containing " + ", ".join(keywords)
        else:
            replacement = " equals " + substring
        parsed_cond = parsed_cond.replace(regexp.group(0), replacement)

    # replace subquery name with table name
    for key in table_subquery_name_pair:
        while key in parsed_cond:
            parsed_cond = parsed_cond.replace(key, table_subquery_name_pair[key])

    return parsed_cond


def parse_cond(cond_name, cond, table_subquery_name_pair):
    # handle single string
    if cond_name in ["Hash Cond", "Join Filter", "Table Filter", "Recheck Cond"]:
        parsed_cond = parse_single_string(cond, table_subquery_name_pair)

    # handle list
    elif cond_name in ["Sort Key", "Group Key"]:
        parsed_cond = []
        for c in cond:
            parsed_cond.append(parse_single_string(c, table_subquery_name_pair))

        parsed_cond = ", ".join(parsed_cond)
    elif isinstance(cond, str):
        parsed_cond = cond
    return parsed_cond