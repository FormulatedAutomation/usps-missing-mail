import os
from dotenv import load_dotenv

from RPA.Dialogs import Dialogs

from tasks.usps import run, get_wicksly_info


def main():
    d = Dialogs()
    d.create_form('questions')
    d.add_text_input(label='Order Lookup', name='tracking_number')
    response = d.request_response()
    tracking_number = response['tracking_number']
    shipment_info = get_wicksly_info(tracking_number)
    run(tracking_number, shipment_info)


if __name__ == "__main__":
    load_dotenv()
    main()
