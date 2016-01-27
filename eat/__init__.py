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
        'name': 'parent_social_security_income',
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
        'name': 'spending_money_income',
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
        'name': 'other_friend_income',
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

adult_earnings_workflow = {
    'adult_salary': {
        'name': 'adult_salary',
        'order': 1,
        'title': 'Salary',
        'value_field': 'salary',
        'frequency_field': 'salary_frequency',
        'headline': 'Does {} receive salary from a job?',
        'next_page': {
            'name': 'adult_wages',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'adults',
            'has_adult_id': False
        },
        'help_tip': "this is salary page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'adult_wages': {
        'name': 'adult_wages',
        'order': 2,
        'title': 'Wages',
        'value_field': 'wages',
        'frequency_field': 'wages_frequency',
        'headline': 'Does {} receive wages?',
        'next_page': {
            'name': 'cash_bonuses',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'adult_salary',
            'has_adult_id': True
        },
        'help_tip': "this is adult_wages page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'cash_bonuses': {
        'name': 'cash_bonuses',
        'order': 3,
        'title': 'Cash Bonuses',
        'value_field': 'cash_bonuses',
        'frequency_field': 'cash_bonuses_frequency',
        'headline': 'Does {} receive cash bonus?',
        'next_page': {
            'name': 'self_employment_income',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'adult_wages',
            'has_adult_id': True
        },
        'help_tip': "this is cash_bonuses page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'self_employment_income': {
        'name': 'self_employment_income',
        'order': 4,
        'title': 'Self employment',
        'value_field': 'self_employment_income',
        'frequency_field': 'self_employment_income_frequency',
        'headline': 'Does {} receive income from self employment?',
        'next_page': {
            'name': 'strike_benefits',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'cash_bonuses',
            'has_adult_id': True
        },
        'help_tip': "this is self_employment page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'strike_benefits': {
        'name': 'strike_benefits',
        'order': 5,
        'title': 'Strike Benefits',
        'value_field': 'strike_benefits',
        'frequency_field': 'strike_benefits_frequency',
        'headline': 'Does {} receive income from strike benefits?',
        'next_page': {
            'name': 'unemployment_insurance',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'self_employment_income',
            'has_adult_id': True
        },
        'help_tip': "this is strike_benefits page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'unemployment_insurance': {
        'name': 'unemployment_insurance',
        'order': 6,
        'title': 'Unemployment Insurance',
        'value_field': 'unemployment_insurance',
        'frequency_field': 'unemployment_insurance_frequency',
        'headline': 'Does {} receive unemployment insurance?',
        'next_page': {
            'name': 'other_earned_income',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'strike_benefits',
            'has_adult_id': True
        },
        'help_tip': "this is unemployment insurance page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'other_earned_income': {
        'name': 'other_earned_income',
        'order': 7,
        'title': 'Other earned income',
        'value_field': 'other_earned_income',
        'frequency_field': 'other_earned_income_frequency',
        'headline': 'Does {} have other earned income?',
        'next_page': {
            'name': 'military_basic_pay',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'unemployment_insurance',
            'has_adult_id': True
        },
        'help_tip': "this is Other earned income page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'military_basic_pay': {
        'name': 'military_basic_pay',
        'order': 8,
        'title': 'Military basic pay',
        'value_field': 'military_basic_pay',
        'frequency_field': 'military_basic_pay_frequency',
        'headline': 'Does {} get military basic pay?',
        'next_page': {
            'name': 'military_bonus',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'unemployment_insurance',
            'has_adult_id': True
        },
        'help_tip': "this is military_basic_pay page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'military_bonus': {
        'name': 'military_bonus',
        'order': 9,
        'title': 'Military bonus',
        'value_field': 'military_bonus',
        'frequency_field': 'military_bonus_frequency',
        'headline': 'Does {} get military bonus?',
        'next_page': {
            'name': 'military_allowance',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'military_basic_pay',
            'has_adult_id': True
        },
        'help_tip': "this is military_basic_pay page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'military_allowance': {
        'name': 'military_allowance',
        'order': 10,
        'title': 'Military allowance',
        'value_field': 'military_allowance',
        'frequency_field': 'military_allowance_frequency',
        'headline': 'Does {} get military allowance?',
        'next_page': {
            'name': 'military_food',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'military_bonus',
            'has_adult_id': True
        },
        'help_tip': "this is military_allowance page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'military_food': {
        'name': 'military_food',
        'order': 11,
        'title': 'Military food',
        'value_field': 'military_food',
        'frequency_field': 'military_food_frequency',
        'headline': 'Does {} get military food?',
        'next_page': {
            'name': 'military_clothing',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'military_bonus',
            'has_adult_id': True
        },
        'help_tip': "this is military_food page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'military_clothing': {
        'name': 'military_clothing',
        'order': 12,
        'title': 'Military clothing',
        'value_field': 'military_clothing',
        'frequency_field': 'military_clothing_frequency',
        'headline': 'Does {} get military clothing?',
        'next_page': {
            'name': 'general_assistance',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'military_food',
            'has_adult_id': True
        },
        'help_tip': "this is military_clothing page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'general_assistance': {
        'name': 'general_assistance',
        'order': 13,
        'title': 'General Assistance',
        'value_field': 'general_assistance',
        'frequency_field': 'general_assistance_frequency',
        'headline': 'Does {} get general assistance?',
        'next_page': {
            'name': 'other_assistance',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'military_clothing',
            'has_adult_id': True
        },
        'help_tip': "this is general_assistance page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'other_assistance': {
        'name': 'other_assistance',
        'order': 14,
        'title': 'Other Assistance',
        'value_field': 'other_assistance',
        'frequency_field': 'other_assistance_frequency',
        'headline': 'Does {} get other assistance?',
        'next_page': {
            'name': 'alimony',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'general_assistance',
            'has_adult_id': True
        },
        'help_tip': "this is other_assistance page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'alimony': {
        'name': 'alimony',
        'order': 15,
        'title': 'Alimony',
        'value_field': 'alimony',
        'frequency_field': 'alimony_frequency',
        'headline': 'Does {} get Alimony?',
        'next_page': {
            'name': 'child_support',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'other_assistance',
            'has_adult_id': True
        },
        'help_tip': "this is alimony page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'child_support': {
        'name': 'child_support',
        'order': 16,
        'title': 'Child Support',
        'value_field': 'child_support',
        'frequency_field': 'child_support_frequency',
        'headline': 'Does {} get any Child Support?',
        'next_page': {
            'name': 'social_security_income',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'alimony',
            'has_adult_id': True
        },
        'help_tip': "this is child support page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'social_security_income': {
        'name': 'social_security_income',
        'order': 17,
        'title': 'Social Security Income',
        'value_field': 'social_security_income',
        'frequency_field': 'social_security_income_frequency',
        'headline': 'Does {} get any Social Security Income?',
        'next_page': {
            'name': 'railroad_income',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'child_support',
            'has_adult_id': True
        },
        'help_tip': "this is social security income page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'railroad_income': {
        'name': 'railroad_income',
        'order': 18,
        'title': 'Railroad Income',
        'value_field': 'railroad_income',
        'frequency_field': 'railroad_income_frequency',
        'headline': 'Does {} get any Railroad Income?',
        'next_page': {
            'name': 'pension_income',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'social_security_income',
            'has_adult_id': True
        },
        'help_tip': "this is railroad income page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'pension_income': {
        'name': 'pension_income',
        'order': 19,
        'title': 'Pension Income',
        'value_field': 'pension_income',
        'frequency_field': 'pension_income_frequency',
        'headline': 'Does {} get any Pension Income?',
        'next_page': {
            'name': 'annuity_income',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'railroad_income',
            'has_adult_id': True
        },
        'help_tip': "this is pension income page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'annuity_income': {
        'name': 'annuity_income',
        'order': 20,
        'title': 'Annuity Income',
        'value_field': 'annuity_income',
        'frequency_field': 'annuity_income_frequency',
        'headline': 'Does {} get any Annuity Income?',
        'next_page': {
            'name': 'survivors_benefits',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'pension_income',
            'has_adult_id': True
        },
        'help_tip': "this is pension income page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'survivors_benefits': {
        'name': 'survivors_benefits',
        'order': 21,
        'title': 'Survivors Benefits',
        'value_field': 'survivors_benefits',
        'frequency_field': 'survivors_benefits_frequency',
        'headline': 'Does {} get any Survivors Benefits?',
        'next_page': {
            'name': 'ssi_disability_benefits',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'annuity_income',
            'has_adult_id': True
        },
        'help_tip': "this is survivors income page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'ssi_disability_benefits': {
        'name': 'ssi_disability_benefits',
        'order': 22,
        'title': 'Disability Benefits From Supplemental Security Income',
        'value_field': 'ssi_disability_benefits',
        'frequency_field': 'ssi_disability_benefits_frequency',
        'headline': 'Does {} get disability benefits from Supplemental Security Income?',
        'next_page': {
            'name': 'private_disability_benefits',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'survivors_benefits',
            'has_adult_id': True
        },
        'help_tip': "this is ssi_disability_benefits income page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'private_disability_benefits': {
        'name': 'private_disability_benefits',
        'order': 23,
        'title': 'Private Disability Benefits',
        'value_field': 'private_disability_benefits',
        'frequency_field': 'private_disability_benefits_frequency',
        'headline': 'Does {} get private disability benefits?',
        'next_page': {
            'name': 'black_lung_benefits',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'ssi_disability_benefits',
            'has_adult_id': True
        },
        'help_tip': "this is private_disability_benefits income page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'black_lung_benefits': {
        'name': 'black_lung_benefits',
        'order': 24,
        'title': 'Black Lung Benefits',
        'value_field': 'black_lung_benefits',
        'frequency_field': 'black_lung_benefits_frequency',
        'headline': 'Does {} get Black Lung Benefits?',
        'next_page': {
            'name': 'workers_compensation',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'private_disability_benefits',
            'has_adult_id': True
        },
        'help_tip': "this is black_lung_benefits income page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'workers_compensation': {
        'name': 'workers_compensation',
        'order': 25,
        'title': 'Workers Compensation',
        'value_field': 'workers_compensation',
        'frequency_field': 'workers_compensation_frequency',
        'headline': 'Does {} get worker''s compensation?',
        'next_page': {
            'name': 'veterans_benefits',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'black_lung_benefits',
            'has_adult_id': True
        },
        'help_tip': "this is workers_compensation income page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'veterans_benefits': {
        'name': 'veterans_benefits',
        'order': 26,
        'title': 'Veterans Benefits',
        'value_field': 'veterans_benefits',
        'frequency_field': 'veterans_benefits_frequency',
        'headline': 'Does {} get Veterans Benefits?',
        'next_page': {
            'name': 'other_retirement_sources',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'workers_compensation',
            'has_adult_id': True
        },
        'help_tip': "this is veterans_benefits income page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'other_retirement_sources': {
        'name': 'other_retirement_sources',
        'order': 27,
        'title': 'Other Retirement Sources',
        'value_field': 'other_retirement_sources',
        'frequency_field': 'other_retirement_sources_frequency',
        'headline': 'Does {} have any other retirement sources?',
        'next_page': {
            'name': 'interest_income',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'veterans_benefits',
            'has_adult_id': True
        },
        'help_tip': "this is other retirement income page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'interest_income': {
        'name': 'interest_income',
        'order': 28,
        'title': 'Other Retirement Sources',
        'value_field': 'interest_income',
        'frequency_field': 'interest_income_frequency',
        'headline': 'Does {} have any income from interest?',
        'next_page': {
            'name': 'dividends',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'other_retirement_sources',
            'has_adult_id': True
        },
        'help_tip': "this is interest income page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'dividends': {
        'name': 'dividends',
        'order': 29,
        'title': 'Dividends',
        'value_field': 'dividends',
        'frequency_field': 'dividends_frequency',
        'headline': 'Does {} have any income dividends?',
        'next_page': {
            'name': 'trust_or_estates_income',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'interest_income',
            'has_adult_id': True
        },
        'help_tip': "this is dividends page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'trust_or_estates_income': {
        'name': 'trust_or_estates_income',
        'order': 30,
        'title': 'Trust or Estates Income',
        'value_field': 'trust_or_estates_income',
        'frequency_field': 'trust_or_estates_income_frequency',
        'headline': 'Does {} have any income from trust or estates?',
        'next_page': {
            'name': 'rental_income',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'dividends',
            'has_adult_id': True
        },
        'help_tip': "this is trust_or_estates_income page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'rental_income': {
        'name': 'rental_income',
        'order': 31,
        'title': 'Rental Income',
        'value_field': 'rental_income',
        'frequency_field': 'rental_income_frequency',
        'headline': 'Does {} have any rental income?',
        'next_page': {
            'name': 'royalties_income',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'trust_or_estates_income',
            'has_adult_id': True
        },
        'help_tip': "this is rental_income page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'royalties_income': {
        'name': 'royalties_income',
        'order': 32,
        'title': 'Royalties Income',
        'value_field': 'royalties_income',
        'frequency_field': 'royalties_income_frequency',
        'headline': 'Does {} have any income from royalties?',
        'next_page': {
            'name': 'prize_winnings',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'rental_income',
            'has_adult_id': True
        },
        'help_tip': "this is royalties_income page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'prize_winnings': {
        'name': 'prize_winnings',
        'order': 33,
        'title': 'Prize Winnings',
        'value_field': 'prize_winnings',
        'frequency_field': 'prize_winnings_frequency',
        'headline': 'Does {} have any income from prize winnings?',
        'next_page': {
            'name': 'savings_withdrawn',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'royalties_income',
            'has_adult_id': True
        },
        'help_tip': "this is prize_winnings page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'savings_withdrawn': {
        'name': 'savings_withdrawn',
        'order': 34,
        'title': 'Savings Withdrawn',
        'value_field': 'savings_withdrawn',
        'frequency_field': 'savings_withdrawn_frequency',
        'headline': 'Does {} withdraw savings?',
        'next_page': {
            'name': 'cash_gifts',
            'has_adult_id': True
        },
        'previous_page': {
            'name': 'prize_winnings',
            'has_adult_id': True
        },
        'help_tip': "this is savings_withdrawn page",
        'template': 'eat/user/application/adult/earnings.html'
    },
    'cash_gifts': {
        'name': 'cash_gifts',
        'order': 35,
        'title': 'Cash Gifts',
        'value_field': 'cash_gifts',
        'frequency_field': 'cash_gifts_frequency',
        'headline': 'Does {} get cash gifts from friends?',
        'next_page': {
            'name': 'adults',
            'has_adult_id': False
        },
        'previous_page': {
            'name': 'savings_withdrawn',
            'has_adult_id': True
        },
        'help_tip': "this is cash gifts page",
        'template': 'eat/user/application/adult/earnings.html'
    }

}
