child_earnings_workflow = {
    'child_salary': {
        'name': 'child_salary',
        'order': 1,
        'title': 'Salary',
        'value_field': 'salary',
        'frequency_field': 'salary_frequency',
        'headline': 'Does {} earn salary or wages from a job?',
        'next_page': {
            'name': 'child_social_security_income',
            'has_child_id': True
        },
        'previous_page': {
            'name': 'children',
            'has_child_id': False
        },
        'help_tip': "this is test",
        'template': 'eat/user/application/child/earnings.html'
    },
    'child_social_security_income': {
        'name': 'child_social_security_income',
        'order': 2,
        'title': 'Disability Payments',
        'value_field': 'ssi_disability',
        'frequency_field': 'ssi_disability_frequency',
        'headline': 'Does {} earn a Social Security benefits for blindness or disability?',
        'next_page': {
            'name': 'parent_social_security_income',
            'has_child_id': True
        },
        'previous_page': {
            'name': 'child_salary',
            'has_child_id': True
        },
        'help_tip': None,
        'template': 'eat/user/application/child/earnings.html'
    },
    'parent_social_security_income': {
        'name':'parent_social_security_income',
        'order': 3,
        'title': 'Survivor’s Benefits',
        'value_field': 'ssi_parent_disability',
        'frequency_field': 'ssi_parent_disability_frequency',
        'headline': 'Does {} receive Social Security benefits because a parent is disabled?',
        'next_page': {
            'name': 'spending_money_income',
            'has_child_id': True
        },
        'previous_page': {
            'name': 'child_social_security_income',
            'has_child_id': True
        },
        'help_tip': None,
        'template': 'eat/user/application/child/earnings.html'
    },
    'spending_money_income': {
        'name':'spending_money_income',
        'order': 4,
        'title': 'Spending Money',
        'value_field': 'spending_money_income',
        'frequency_field': 'spending_money_income_frequency',
        'headline': 'Does a friend or extended family member regularly give spending money to {}',
        'next_page': {
            'name': 'other_friend_income',
            'has_child_id': True
        },
        'previous_page': {
            'name': 'parent_social_security_income',
            'has_child_id': True
        },
        'help_tip': None,
        'template': 'eat/user/application/child/earnings.html'
    },
    'other_friend_income': {
        'name':'other_friend_income',
        'order': 5,
        'title': 'Other income from friends',
        'value_field': 'other_friend_income',
        'frequency_field': 'other_friend_income_frequency',
        'headline': "Does {} receive any other income on regular basis from friends?",
        'next_page': {
            'name': 'pension_income',
            'has_child_id': True
        },
        'previous_page': {
            'name': 'spending_money_income',
            'has_child_id': True
        },
        'help_tip': None,
        'template': 'eat/user/application/child/earnings.html'
    },
    'pension_income': {
        'name': 'pension_income',
        'order': 6,
        'title': 'Pension funds',
        'value_field': 'pension_income',
        'frequency_field': 'pension_income_frequency',
        'headline': "Does {} receive income from a private pension fund?",
        'next_page': {
            'name': 'annuity_income',
            'has_child_id': True
        },
        'previous_page': {
            'name': 'other_friend_income',
            'has_child_id': True
        },
        'help_tip': None,
        'template': 'eat/user/application/child/earnings.html'
    },
    'annuity_income': {
        'name': 'annuity_income',
        'order': 7,
        'title': 'Annuity',
        'value_field': 'annuity_income',
        'frequency_field': 'annuity_income_frequency',
        'headline': "Does {} receive Annuity?",
        'next_page': {
            'name': 'trust_income',
            'has_child_id': True
        },
        'previous_page': {
            'name': 'pension_income',
            'has_child_id': True
        },
        'help_tip': None,
        'template': 'eat/user/application/child/earnings.html'
    },
    'trust_income': {
        'name': 'trust_income',
        'order': 8,
        'title': 'Private Trust income',
        'value_field': 'trust_income',
        'frequency_field': 'trust_income_frequency',
        'headline': "Does {} receive income from private trust?",
        'next_page': {
            'name': 'other_income',
            'has_child_id': True
        },
        'previous_page': {
            'name': 'annuity_income',
            'has_child_id': True
        },
        'help_tip': None,
        'template': 'eat/user/application/child/earnings.html'
    },
    'other_income': {
        'name': 'other_income',
        'order': 9,
        'title': 'Any other income',
        'value_field': 'other_income',
        'frequency_field': 'other_income_frequency',
        'headline': "Does {} receive any other income?",
        'next_page': {
            'name': 'children',
            'has_child_id': False
        },
        'previous_page': {
            'name': 'trust_income',
            'has_child_id': True
        },
        'help_tip': None,
        'template': 'eat/user/application/child/earnings.html'
    }
}