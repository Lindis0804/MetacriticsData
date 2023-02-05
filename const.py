link = "https://www.metacritic.com/browse/movies/score/metascore/all/filtered?sort=desc&page="
rating_list_css = "span[class='based_on']"
year_css = "span[class='release_year lighter']"
title_css = "div[class='product_page_title oswald']"
distributor_css = "span[class='distributor']"
release_date_css = "span[class='release_date']"
num_of_critic_by_level_css = "div[class='count fr']"
image_css = "img[class='summary_img']"
critic_score_css = [
    "span[class='metascore_w larger movie positive perfect']",
    "span[class='metascore_w larger movie positive']",
    "span[class='metascore_w larger movie mixed']",
    "span[class='metascore_w larger movie negative']"
]
rating_score_css = [
    "span[class='metascore_w user larger movie positive']",
    "span[class='metascore_w user larger movie mixed']",
    "span[class='metascore_w user larger movie negative']"
]
stars_css = "div[class='summary_cast details_section']"
facts_css = "span[class='summary_notes']"
summary_css = "div[class='summary_deck details_section']"
director_css = "div[class='director']"
genres_css = "div[class='genres']"
rating_css = "div[class='rating']"
runtime_css = "div[class='runtime']"


def convert(s):
    if (s.__contains__(",")):
        res = int("".join(s.split(",")))
    else:
        res = int(s)
    return res
#in the next time, increase film-serial to 1
film = {
    'page':78,
    'fillm-serial':99
}
print(convert("1,2323425"))
