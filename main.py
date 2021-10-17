from work_module import *

if __name__ == "__main__":
    create_table_people()
    records_generator()
    add_2_wachowski()
    amend_gender_for_wachowski_or_any_other_by_surname()
    amend_name_by_name_and_surname()
    amend_name_by_name_and_surname('Andrew', 'Wachowski', 'Lilly')
    fill_empty_emails()
    choose_people_by_salary()
    choose_people_by_salary_and_age()
    delete_records_by_empty_field()