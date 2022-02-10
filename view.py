import eel
import desktop
import task2

app_name="html"
end_point="index.html"
size=(700,780)

@ eel.expose
def main(search_keyword, is_option: bool = False, page_limit: int=1, hidden_chrome: bool=False):
    task2.main(search_keyword)
    
    return True


desktop.start(app_name,end_point,size)