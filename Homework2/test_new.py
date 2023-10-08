import yaml
from module import Site
import time

with open("./config.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])


def test_new_post(x_selector1, x_selector2, x_selector4, btn_selector, account_name, butt_post, name_post,
                  save_post, check_name, title_name):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(testdata["pswd"])
    btn = site.find_element("css", btn_selector)
    btn.click()
    time.sleep(testdata["sleep_time"])
    butt = site.find_element("xpath", butt_post)
    butt.click()
    post = site.find_element("xpath", name_post)
    post.clear()
    post.send_keys(testdata["tlt"])
    btn3 = site.find_element("xpath", save_post)
    btn3.click()

    time.sleep(testdata["sleep_time"])

    code_label = site.find_element("xpath", check_name).text
    assert code_label == title_name, "test 'test_new_post' Failed"

    site.driver.close()
