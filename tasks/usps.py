import os

from playwright import sync_playwright
from RPA.Robocloud.Secrets import Secrets

ORIGIN_COMPANY = os.environ.get('ORIGIN_COMPANY')
ORIGIN_STREET = os.environ.get('ORIGIN_STREET')
ORIGIN_ZIP = os.environ.get('ORIGIN_ZIP')
ORIGIN_CITY = os.environ.get('ORIGIN_CITY')
ORIGIN_STATE = os.environ.get('ORIGIN_STATE')
ORIGIN_PHONE = os.environ.get('ORIGIN_PHONE')

CONTACT_EMAIL = os.environ.get('CONTACT_EMAIL')
CONTACT_FIRST = os.environ.get('CONTACT_FIRST')
CONTACT_LAST = os.environ.get('CONTACT_LAST')


def get_wicksly_info(tracking_number):
    secrets = Secrets()
    USER_NAME = secrets.get_secret("credentials")["PLATFORM_USERNAME"]
    PASSWORD = secrets.get_secret("credentials")["PLATFORM_PASS"]
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        wicksly_context = browser.newContext()
        w_page = wicksly_context.newPage()
        w_page.goto(os.environ.get('PLATFORM_URL'))
        w_page.fill('#id_username', USER_NAME)
        w_page.fill('#id_password', PASSWORD)
        with w_page.expect_navigation():
            w_page.click('input[type=submit]')
        w_page.goto(os.environ.get('PLATFORM_URL'))
        w_page.fill('#searchbar', tracking_number)

        with w_page.expect_navigation():
            w_page.click('text=Search')

        w_page.querySelectorAll('table#result_list tbody tr a')[0].click()
        street = w_page.getAttribute('#id_street1', 'value')
        city = w_page.getAttribute('#id_city', 'value')
        state = w_page.getAttribute('#id_state', 'value')
        postal_code = w_page.getAttribute('#id_postal_code', 'value')

        return {
            'street': street,
            'city': city,
            'state': state,
            'postal_code': postal_code
        }


def run(tracking_number, shipment_info):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.newContext()
        page = context.newPage()
        page.goto('https://www.usps.com/help/missing-mail.htm')
        page.click("text=\"Start Your Form\"")
        page.fill("input[type=\"text\"]", tracking_number)
        with page.expect_navigation():
            page.click("text=\"Track\"")

        page.click("text=\"Start\"")
        page.click("a[role=\"button\"]")
        page.click(
            "//a[normalize-space(.)='Package' and normalize-space(@title)='Package' and normalize-space(@role)='menuitemradio']")
        page.click(
            "//a[normalize-space(.)='--None--' and normalize-space(@role)='button']")

        # Click //a[normalize-space(.)='First-Class Mail®' and normalize-space(@title)='First-Class Mail®' and normalize-space(@role)='menuitemradio']
        page.click(
            "//a[normalize-space(.)='First-Class Mail®' and normalize-space(@title)='First-Class Mail®' and normalize-space(@role)='menuitemradio']")

        # Click //a[normalize-space(.)='--None--' and normalize-space(@role)='button']
        page.click(
            "//a[normalize-space(.)='--None--' and normalize-space(@role)='button']")

        # Click //a[normalize-space(.)='Business' and normalize-space(@title)='Business' and normalize-space(@role)='menuitemradio']
        page.click(
            "//a[normalize-space(.)='Business' and normalize-space(@title)='Business' and normalize-space(@role)='menuitemradio']")

        # Click //a[normalize-space(.)='--None--' and normalize-space(@role)='button']
        page.click(
            "//a[normalize-space(.)='--None--' and normalize-space(@role)='button']")

        # Click (//a[normalize-space(.)='Residence' and normalize-space(@title)='Residence' and normalize-space(@role)='menuitemradio'])[2]
        page.click(
            "(//a[normalize-space(.)='Residence' and normalize-space(@title)='Residence' and normalize-space(@role)='menuitemradio'])[2]")

        # Check //div[normalize-space(.)='None']/input[normalize-space(@type)='checkbox']
        page.check(
            "//div[normalize-space(.)='None']/input[normalize-space(@type)='checkbox']")

        # Click //div[normalize-space(.)='Unknown' and normalize-space(@role)='option']
        page.click(
            "//div[normalize-space(.)='Unknown' and normalize-space(@role)='option']")

        # Click //lightning-primitive-icon
        page.click("//lightning-primitive-icon")

        # Click input[type="text"]
        page.click("input[type=\"text\"]")

        # Fill input[type="text"]
        page.fill("input[type=\"text\"]", "15")

        # Click text="Next"
        page.click("text=\"Next\"")

        page.waitForSelector(
            "//label[span[text()='Street Address']]/following-sibling::input")

        page.click(
            "//label[span[text()='Street Address']]/following-sibling::input")

        page.fill(
            "//label[span[text()='Street Address']]/following-sibling::input", ORIGIN_STREET)

        # Click //div[normalize-space(.)='City']/input[normalize-space(@type)='text']
        page.click(
            "//div[normalize-space(.)='City']/input[normalize-space(@type)='text']")

        # Fill //div[normalize-space(.)='City']/input[normalize-space(@type)='text']
        page.fill(
            "//div[normalize-space(.)='City']/input[normalize-space(@type)='text']", ORIGIN_CITY)

        page.click(
            "//div[normalize-space(@role)='list']/div[4]/div[1][normalize-space(@role)='listitem']/div/div/div/div/div[1]/div/div/a[normalize-space(.)='--None--' and normalize-space(@role)='button']")

        page.click(
            f"//a[normalize-space(.)='{ORIGIN_STATE}' and normalize-space(@title)='{ORIGIN_STATE}' and normalize-space(@role)='menuitemradio']")

        page.click(
            "//div[normalize-space(.)='ZIP Code™']/input[normalize-space(@type)='text']")

        # Click //div[normalize-space(.)='ZIP Code™']/input[normalize-space(@type)='text']
        page.click(
            "//div[normalize-space(.)='ZIP Code™']/input[normalize-space(@type)='text']")

        # Fill //div[normalize-space(.)='ZIP Code™']/input[normalize-space(@type)='text']
        page.fill(
            "//div[normalize-space(.)='ZIP Code™']/input[normalize-space(@type)='text']", ORIGIN_ZIP)

        page.waitForSelector(
            "//div[normalize-space(.)='Street Address*']/input[normalize-space(@type)='text']")
        # Click //div[normalize-space(.)='Street Address*']/input[normalize-space(@type)='text']
        page.click(
            "//div[normalize-space(.)='Street Address*']/input[normalize-space(@type)='text']")

        # Fill //div[normalize-space(.)='Street Address*']/input[normalize-space(@type)='text']
        page.fill(
            "//div[normalize-space(.)='Street Address*']/input[normalize-space(@type)='text']", shipment_info['street'])

        # Click (//div[normalize-space(@role)='listitem']/div/div/div[normalize-space(.)='Apt/Suite/Other']/input[normalize-space(@type)='text'])[2]
        page.click(
            "(//div[normalize-space(@role)='listitem']/div/div/div[normalize-space(.)='Apt/Suite/Other']/input[normalize-space(@type)='text'])[2]")
        page.click(
            "//div[normalize-space(.)='City*']/input[normalize-space(@type)='text']")
        page.fill(
            "//div[normalize-space(.)='City*']/input[normalize-space(@type)='text']", shipment_info['city'])
        page.click(
            "(//div[normalize-space(@role)='listitem']/div/div/div/div/div[1]/div/div/a[normalize-space(.)='--None--' and normalize-space(@role)='button'])[2]")

        page.querySelectorAll(f"//a[starts-with(@title, '{shipment_info['state']}') and normalize-space(@role)='menuitemradio']")[1].click()
        page.click(
            "//div[normalize-space(.)='ZIP Code™*']/input[normalize-space(@type)='text']")
        page.fill(
            "//div[normalize-space(.)='ZIP Code™*']/input[normalize-space(@type)='text']", shipment_info['postal_code'])

        page.click("text=\"Next\"")
        page.waitForSelector(
            "//div[normalize-space(.)='First Name*']/input[normalize-space(@type)='text']")
        page.fill(
            "//div[normalize-space(.)='First Name*']/input[normalize-space(@type)='text']", CONTACT_FIRST)
        page.fill(
            "//div[normalize-space(.)='Middle Name']/input[normalize-space(@type)='text']", "")
        page.press(
            "//div[normalize-space(.)='Middle Name']/input[normalize-space(@type)='text']", "Tab")
        page.fill(
            "//div[normalize-space(.)='Last Name*']/input[normalize-space(@type)='text']", CONTACT_LAST)
        page.press(
            "//div[normalize-space(.)='Last Name*']/input[normalize-space(@type)='text']", "Tab")
        page.fill(
            "(//div[normalize-space(@role)='listitem']/div/div/div[normalize-space(.)='Street Address*']/input[normalize-space(@type)='text'])[2]",
            ORIGIN_STREET)
        page.click(
            "(//div[normalize-space(@role)='listitem']/div/div/div[normalize-space(.)='City*']/input[normalize-space(@type)='text'])[2]")
        page.fill(
            "(//div[normalize-space(@role)='listitem']/div/div/div[normalize-space(.)='City*']/input[normalize-space(@type)='text'])[2]",
            ORIGIN_CITY)
        page.click(
            "(//div[normalize-space(@role)='listitem']/div/div/div/div/div[1]/div/div/a[normalize-space(.)='--None--' and normalize-space(@role)='button'])[2]")
        page.click(
            f"(//a[normalize-space(.)='{ORIGIN_STATE}' and normalize-space(@title)='{ORIGIN_STATE}' and normalize-space(@role)='menuitemradio'])[3]")
        page.click(
            "(//div[normalize-space(@role)='listitem']/div/div/div[normalize-space(.)='ZIP Code™*']/input[normalize-space(@type)='text'])[2]")
        page.fill(
            "(//div[normalize-space(@role)='listitem']/div/div/div[normalize-space(.)='ZIP Code™*']/input[normalize-space(@type)='text'])[2]",
            ORIGIN_ZIP)

        page.click(
            "//div[normalize-space(.)='Email*']/input[normalize-space(@type)='text']")
        page.fill(
            "//div[normalize-space(.)='Email*']/input[normalize-space(@type)='text']", CONTACT_EMAIL)
        page.press(
            "//div[normalize-space(.)='Email*']/input[normalize-space(@type)='text']", "Tab")
        page.fill(
            "//div[normalize-space(.)='Retype Email*']/input[normalize-space(@type)='text']", CONTACT_EMAIL)
        page.press(
            "//div[normalize-space(.)='Retype Email*']/input[normalize-space(@type)='text']", "Tab")
        page.fill("input[type=\"tel\"]", ORIGIN_PHONE)
        page.click(
            "(//div[normalize-space(@role)='listitem']/div/div/div/div/div[1]/div/div/a[normalize-space(.)='--None--' and normalize-space(@role)='button'])[2]")
        page.click(
            "(//a[normalize-space(.)='Business' and normalize-space(@title)='Business' and normalize-space(@role)='menuitemradio'])[3]")
        page.click(
            "//div[normalize-space(.)='Company']/input[normalize-space(@type)='text']")
        page.fill(
            "//div[normalize-space(.)='Company']/input[normalize-space(@type)='text']", ORIGIN_COMPANY)
        page.click("//div[normalize-space(.)='PreviousFinishCancel']")

        page.click("text=\"Finish\"")
        page.click("text=\"Submit\"")
        page.close()
        context.close()
        browser.close()
