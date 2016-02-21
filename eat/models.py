from django.db import models
from django.contrib.auth.models import User
import datetime
import uuid

APPLICATION_STATUSES = (
    (0, 'Start'),
    (1, 'Step 1'),
    (2, 'Complete'),
)


YES_NO = (
    (True, 'Yes',),
    (False, 'No',)
)

STATES = (
    ('AL', 'Alabama',),
    ('AK', 'Alaska',),
    ('AZ', 'Arizona',),
    ('AR', 'Arkansas',),
    ('CA', 'California',),
    ('CO', 'Colorado',),
    ('CT', 'Connecticut',),
    ('DE', 'Delaware',),
    ('FL', 'Florida',),
    ('GA', 'Georgia',),
    ('HI', 'Hawaii',),
    ('ID', 'Idaho',),
    ('IL', 'Illinois',),
    ('IN', 'Indiana',),
    ('IA', 'Iowa',),
    ('KS', 'Kansas',),
    ('KY', 'Kentucky',),
    ('LA', 'Louisiana',),
    ('ME', 'Maine',),
    ('MD', 'Maryland',),
    ('MA', 'Massachusetts',),
    ('MI', 'Michigan',),
    ('MN', 'Minnesota',),
    ('MS', 'Mississippi',),
    ('MO', 'Missouri',),
    ('MT', 'Montana',),
    ('NE', 'Nebraska',),
    ('NV', 'Nevada',),
    ('NH', 'New Hampshire',),
    ('NJ', 'New Jersey',),
    ('NM', 'New Mexico',),
    ('NY', 'New York',),
    ('NC', 'North Carolina',),
    ('ND', 'North Dakota',),
    ('OH', 'Ohio',),
    ('OK', 'Oklahoma',),
    ('OR', 'Oregon',),
    ('PA', 'Pennsylvania',),
    ('RI', 'Rhode Island',),
    ('SC', 'South Carolina',),
    ('SD', 'South Dakota',),
    ('TN', 'Tennessee',),
    ('TX', 'Texas',),
    ('UT', 'Utah',),
    ('VT', 'Vermont',),
    ('VA', 'Virginia',),
    ('WA', 'Washington',),
    ('WV', 'West Virginia',),
    ('WI', 'Wisconsin',),
    ('WY', 'Wyoming',),
)


class Ethnicity(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')

    def __str__(self):
        return self.name


class Application(models.Model):
    applications = models.Manager()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=APPLICATION_STATUSES, verbose_name='Application Status',
                                 help_text='Application Status', default=0)
    last_page = models.CharField(max_length=50, verbose_name='Last Page', blank=True, null=True)
    enabled = models.BooleanField(verbose_name='Enabled', default=True)
    create_date = models.DateField(verbose_name='Create date', default=datetime.date.today)
    modified_date = models.DateField(verbose_name='Last modified date', blank=True, null=True)
    total_children = models.IntegerField(verbose_name='Total Household Children',
                                                  help_text='Total household members who are children',
                                                  blank=True, null=True)
    total_adults = models.IntegerField(verbose_name='Total Household Adults',
                                                  help_text='Total household members who are adults',
                                                  blank=True, null=True)

    assistance_program = models.BooleanField(verbose_name='Participate in Assistance Program', choices=YES_NO,
                                             default=False)
    app_for_foster_child = models.BooleanField(verbose_name='Is this App for Foster Child only?', choices=YES_NO,
                                               default=False)
    ssn_four_digit = models.CharField(max_length=4,
                                      verbose_name='Last 4 digits of SSN',
                                      help_text='Last four digits of the Social Security number of an '
                                                'adult household member',
                                      blank=True,
                                      null=True)
    no_ssn = models.BooleanField(verbose_name='Check if No SSN', default=False)
    case_number = models.CharField(max_length=50,
                                   verbose_name='Case Number', blank=True, null=True)

    first_name = models.CharField(max_length=25,
                                  verbose_name='First Name', blank=True, null=True)
    last_name = models.CharField(max_length=25,
                                 verbose_name='Last Name', blank=True, null=True)
    middle_name = models.CharField(max_length=25,
                                   verbose_name='Middle Name',
                                   blank=True,
                                   null=True)
    signature = models.CharField(max_length=75,
                                 verbose_name='Signature', blank=True, null=True)
    todays_date = models.DateField(verbose_name='Todays Date', blank=True, null=True)
    street_address = models.CharField(max_length=255,
                                      verbose_name='Street Address', blank=True, null=True)
    apt = models.CharField(max_length=10,
                           verbose_name='Apartment Number', blank=True, null=True)
    city = models.CharField(max_length=75,
                            verbose_name='City', blank=True, null=True)
    state = models.CharField(max_length=2, choices=STATES,
                             verbose_name='State', blank=True, null=True)
    zip = models.CharField(max_length=10,
                           verbose_name='Zip', blank=True, null=True)
    phone = models.CharField(max_length=15, verbose_name='Phone', blank=True, null=True)
    email = models.EmailField(max_length=255, verbose_name='Email', blank=True, null=True)
    ethnicity = models.ForeignKey(Ethnicity, blank=True, null=True)
    is_american_indian = models.NullBooleanField(verbose_name='Is American Indian or Alaskan Native')
    is_asian = models.NullBooleanField(verbose_name='Is Asian')
    is_black = models.NullBooleanField(verbose_name='Is Black or African American')
    is_hawaiian = models.NullBooleanField(verbose_name='Is Hawaiian or Other Pacific Islander')
    is_white = models.NullBooleanField(verbose_name='Is White')
    active = models.BooleanField(verbose_name='Active', default=True)
    contact_form_complete = models.BooleanField(verbose_name='Contact form complete', default=False)
    all_adults_entered = models.BooleanField(verbose_name='All adults were entered', default=False)
    all_children_entered = models.BooleanField(verbose_name='All children were entered', default=False)


class PayFrequency(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')

    def __str__(self):
        return self.name


class Child(models.Model):
    children = models.Manager()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25,
                                  verbose_name='First Name')
    last_name = models.CharField(max_length=25,
                                 verbose_name='Last Name')
    middle_name = models.CharField(max_length=25,
                                   verbose_name='Middle Name',
                                   blank=True,
                                   null=True)
    is_student = models.BooleanField(verbose_name='Is Student')
    is_head_start_participant = models.BooleanField(verbose_name='Is Head Start Participant')
    foster_child = models.BooleanField(verbose_name='Is Foster Child')
    hmr = models.BooleanField(verbose_name='Homeless, Migrant, Runaway')
    salary = models.IntegerField(verbose_name='Salary',
                                 help_text='Salary or Wages from a Job',
                                 blank=True,
                                 null=True)
    salary_frequency = models.ForeignKey(PayFrequency, blank=True, null=True, related_name='salary_frequency')
    ssi_disability = models.IntegerField(verbose_name='Social Security Income for Disability',
                                         help_text='Social security income for childs blindness or disability',
                                         blank=True,
                                         null=True)
    ssi_disability_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                 related_name='ssi_disability_frequency')
    ssi_parent_disability = models.IntegerField(verbose_name='Social Security Income for Parents Disability',
                                    help_text='Social security income received if parent is disabled/retired/deceased',
                                    blank=True,
                                    null=True)
    ssi_parent_disability_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                        related_name='ssi_parent_disability_frequency')
    spending_money_income = models.IntegerField(verbose_name='Spending Money Income',
                                                help_text='Spending money received from a person outside the household',
                                                blank=True,
                                                null=True)
    spending_money_income_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                        related_name='spending_money_income_frequency')
    other_friend_income = models.IntegerField(verbose_name='Other Regular Income From Friends',
                                              blank=True,
                                              null=True)
    other_friend_income_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                      related_name='other_friend_income_frequency')
    pension_income = models.IntegerField(verbose_name='Pension Income',
                                         blank=True,
                                         null=True)
    pension_income_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                 related_name='pension_income_frequency')
    annuity_income = models.IntegerField(verbose_name='Annuity Income',
                                         blank=True,
                                         null=True)
    annuity_income_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                 related_name='annuity_income_frequency')
    trust_income = models.IntegerField(verbose_name='Trust Income',
                                       blank=True,
                                       null=True)
    trust_income_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                               related_name='trust_income_frequency')
    other_income = models.IntegerField(verbose_name='Other Income',
                                       help_text='Any other income',
                                       blank=True,
                                       null=True)
    other_income_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                               related_name='other_income_frequency')

    def get_total_earning(self):
        t = 0
        if self.salary is not None:
            t += self.salary

        if self.ssi_disability is not None:
            t += self.ssi_disability

        if self.ssi_parent_disability is not None:
            t += self.ssi_parent_disability

        if self.spending_money_income is not None:
            t += self.spending_money_income

        if self.other_friend_income is not None:
            t += self.other_friend_income

        if self.pension_income is not None:
            t += self.pension_income

        if self.annuity_income is not None:
            t += self.annuity_income

        if self.trust_income is not None:
            t += self.trust_income

        if self.other_income is not None:
            t += self.other_income

        return t


class Adult(models.Model):
    adults = models.Manager()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25,
                                  verbose_name='First Name')
    middle_name = models.CharField(max_length=25,
                                   verbose_name='Middle Name', blank=True, null=True)
    last_name = models.CharField(max_length=25,
                                 verbose_name='Last Name')
    salary = models.IntegerField(verbose_name='Salary',
                                 help_text='Salary from a Job',
                                 blank=True,
                                 null=True)
    salary_frequency = models.ForeignKey(PayFrequency, blank=True, null=True, related_name='adult_salary_frequency')
    wages = models.IntegerField(verbose_name='Wages',
                                help_text='Wages from a Job',
                                blank=True,
                                null=True)
    wages_frequency = models.ForeignKey(PayFrequency, blank=True, null=True, related_name='wages_frequency')
    cash_bonuses = models.IntegerField(verbose_name='Cash Bonuses',
                                       blank=True,
                                       null=True)
    cash_bonuses_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                               related_name='cash_bonuses_frequency')
    self_employment_income = models.IntegerField(verbose_name='Self Employment Income',
                                                 help_text='Net income from self employment',
                                                 blank=True,
                                                 null=True)
    self_employment_income_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                         related_name='self_employment_income_frequency')
    strike_benefits = models.IntegerField(verbose_name='Strike Benefits',
                                          blank=True,
                                          null=True)
    strike_benefits_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                  related_name='strike_benefits_frequency')
    unemployment_insurance = models.IntegerField(verbose_name='Unemployment Insurance',
                                                 blank=True,
                                                 null=True)
    unemployment_insurance_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                         related_name='unemployment_insurance_frequency')
    other_earned_income = models.IntegerField(verbose_name='Other Earned Income',
                                              blank=True,
                                              null=True)
    other_earned_income_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                      related_name='other_earned_income_frequency')
    military_basic_pay = models.IntegerField(verbose_name='Military Basic Pay',
                                             blank=True,
                                             null=True)
    military_basic_pay_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                     related_name='military_basic_pay_frequency')
    military_bonus = models.IntegerField(verbose_name='Military Bonus',
                                         blank=True,
                                         null=True)
    military_bonus_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                 related_name='military_bonus_frequency')
    military_allowance = models.IntegerField(verbose_name='Military Allowance',
                                             blank=True,
                                             null=True)
    military_allowance_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                     related_name='military_allowance_frequency')
    military_food = models.IntegerField(verbose_name='Military Food',
                                        blank=True,
                                        null=True)
    military_food_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                related_name='military_food_frequency')
    military_clothing = models.IntegerField(verbose_name='Military Clothing',
                                            blank=True,
                                            null=True)
    military_clothing_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                    related_name='military_clothing_frequency')
    general_assistance = models.IntegerField(verbose_name='General Assistance',
                                             help_text='General assistance excluding SNAP or TANF',
                                             blank=True,
                                             null=True)
    general_assistance_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                     related_name='general_assistance_frequency')
    cash_assistance = models.IntegerField(verbose_name='Cash assistance from State or local government',
                                           blank=True,
                                           null=True)
    cash_assistance_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                  related_name='cash_assistance_frequency')
    alimony = models.IntegerField(verbose_name='Alimony Received',
                                  blank=True,
                                  null=True)
    alimony_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                          related_name='alimony_frequency')
    child_support = models.IntegerField(verbose_name='Child Support',
                                        blank=True,
                                        null=True)
    child_support_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                related_name='child_support_frequency')
    social_security_income = models.IntegerField(verbose_name='Social Security Income',
                                                 blank=True,
                                                 null=True)
    social_security_income_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                         related_name='social_security_income_frequency')
    railroad_income = models.IntegerField(verbose_name='Railroad Retirement Income',
                                          blank=True,
                                          null=True)
    railroad_income_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                  related_name='railroad_income_frequency')
    pension_income = models.IntegerField(verbose_name='Pension Income',
                                         blank=True,
                                         null=True)
    pension_income_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                 related_name='adult_pension_income_frequency')
    annuity_income = models.IntegerField(verbose_name='Annuity Income',
                                         blank=True,
                                         null=True)
    annuity_income_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                 related_name='adult_annuity_income_frequency')
    survivors_benefits = models.IntegerField(verbose_name='Survivor''s Benefits',
                                             blank=True,
                                             null=True)
    survivors_benefits_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                     related_name='survivors_benefits_frequency')
    ssi_disability_benefits = models.IntegerField(verbose_name='Disability Benefits From Supplemental Security Income',
                                                  blank=True,
                                                  null=True)
    ssi_disability_benefits_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                          related_name='ssi_disability_benefits_frequency')
    private_disability_benefits = models.IntegerField(verbose_name='Private Disability Benefits',
                                                      blank=True,
                                                      null=True)
    private_disability_benefits_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                              related_name='private_disability_benefits_frequency')
    black_lung_benefits = models.IntegerField(verbose_name='Black Lung Benefits',
                                              blank=True,
                                              null=True)
    black_lung_benefits_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                      related_name='black_lung_benefits_frequency')
    workers_compensation = models.IntegerField(verbose_name='Worker''s Compensation',
                                               blank=True,
                                               null=True)
    workers_compensation_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                       related_name='workers_compensation_frequency')
    veterans_benefits = models.IntegerField(verbose_name='Veteran''s Benefits',
                                            blank=True,
                                            null=True)
    veterans_benefits_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                    related_name='veterans_benefits_frequency')
    other_retirement_sources = models.IntegerField(verbose_name='Other Retirement Sources',
                                                   blank=True,
                                                   null=True)
    other_retirement_sources_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                           related_name='other_retirement_sources_frequency')
    interest_income = models.IntegerField(verbose_name='Interest Income',
                                          blank=True,
                                          null=True)
    interest_income_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                  related_name='interest_income_frequency')
    investment_income = models.IntegerField(verbose_name='Investment Income',
                                          blank=True,
                                          null=True)
    investment_income_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                    related_name='investment_income_frequency')
    dividends = models.IntegerField(verbose_name='Dividends',
                                    blank=True,
                                    null=True)
    dividends_frequency = models.ForeignKey(PayFrequency, blank=True, null=True, related_name='dividends_frequency')
    trust_or_estates_income = models.IntegerField(verbose_name='Trust Or Estates Income',
                                                  blank=True,
                                                  null=True)
    trust_or_estates_income_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                          related_name='trust_or_estates_income_frequency')
    rental_income = models.IntegerField(verbose_name='Rental Income',
                                        blank=True,
                                        null=True)
    rental_income_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                related_name='rental_income_frequency')
    royalties_income = models.IntegerField(verbose_name='Royalties Income',
                                           blank=True,
                                           null=True)
    royalties_income_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                   related_name='royalties_income_frequency')
    prize_winnings = models.IntegerField(verbose_name='Prize Winnings',
                                         blank=True,
                                         null=True)
    prize_winnings_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                 related_name='prize_winnings_frequency')
    savings_withdrawn = models.IntegerField(verbose_name='Savings Withdrawn',
                                            blank=True,
                                            null=True)
    savings_withdrawn_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                                    related_name='savings_withdrawn_frequency')
    cash_gifts = models.IntegerField(verbose_name='Cash Gifts from Friends',
                                     blank=True,
                                     null=True)
    cash_gifts_frequency = models.ForeignKey(PayFrequency, blank=True, null=True,
                                             related_name='cash_gifts_frequency')

    def get_total_earning(self):
        t = 0
        t += self.salary if self.salary is not None else 0
        t += self.wages if self.wages is not None else 0
        t += self.cash_bonuses if self.cash_bonuses is not None else 0
        t += self.self_employment_income if self.self_employment_income is not None else 0
        t += self.strike_benefits if self.strike_benefits is not None else 0
        t += self.unemployment_insurance if self.unemployment_insurance is not None else 0
        t += self.other_earned_income if self.other_earned_income is not None else 0
        t += self.military_basic_pay if self.military_basic_pay is not None else 0
        t += self.military_bonus if self.military_bonus is not None else 0
        t += self.military_allowance if self.military_allowance is not None else 0
        t += self.military_food if self.military_food is not None else 0
        t += self.military_clothing if self.military_clothing is not None else 0
        t += self.general_assistance if self.general_assistance is not None else 0
        t += self.cash_assistance if self.cash_assistance is not None else 0
        t += self.alimony if self.alimony is not None else 0
        t += self.child_support if self.child_support is not None else 0
        t += self.social_security_income if self.social_security_income is not None else 0
        t += self.railroad_income if self.railroad_income is not None else 0
        t += self.pension_income if self.pension_income is not None else 0
        t += self.annuity_income if self.annuity_income is not None else 0
        t += self.survivors_benefits if self.survivors_benefits is not None else 0
        t += self.ssi_disability_benefits if self.ssi_disability_benefits is not None else 0
        t += self.private_disability_benefits if self.private_disability_benefits is not None else 0
        t += self.black_lung_benefits if self.black_lung_benefits is not None else 0
        t += self.workers_compensation if self.workers_compensation is not None else 0
        t += self.veterans_benefits if self.veterans_benefits is not None else 0
        t += self.other_retirement_sources if self.other_retirement_sources is not None else 0
        t += self.interest_income if self.interest_income is not None else 0
        t += self.investment_income if self.investment_income is not None else 0
        t += self.dividends if self.dividends is not None else 0
        t += self.trust_or_estates_income if self.trust_or_estates_income is not None else 0
        t += self.rental_income if self.rental_income is not None else 0
        t += self.royalties_income if self.royalties_income is not None else 0
        t += self.prize_winnings if self.prize_winnings is not None else 0
        t += self.savings_withdrawn if self.savings_withdrawn is not None else 0
        t += self.cash_gifts if self.cash_gifts is not None else 0
        return t


class EarningSource(models.Model):
    sources = models.Manager()
    name = models.CharField(max_length=50, verbose_name='Source')

    def __str__(self):
        return self.name


class EarningsPage(models.Model):
    entity = models.CharField(max_length=50,
                                choices=(('child', 'Child',), ('adult', 'Adult',)),
                                verbose_name='Entity')
    name = models.CharField(max_length=50, verbose_name='Page name')
    page_arg = models.CharField(max_length=50,
                                choices=(('child_id', 'child_id',), ('adult_id', 'adult_id',)),
                                verbose_name='Page Argument', blank=True, null=True)
    source = models.ForeignKey(EarningSource, blank=True, null=True)
    page_type = models.CharField(max_length=20,
                                 choices=(('form', 'Form',),
                                          ('confirmation', 'Confirmation',),
                                          ('summary', 'Summary',)),
                                 verbose_name='Page Type', default='form')
    value_field = models.CharField(max_length=50, verbose_name='Value Field', blank=True, null=True)
    frequency_field = models.CharField(max_length=50, verbose_name='Frequency Field', blank=True, null=True)
    display_title = models.CharField(max_length=100, verbose_name='Display Title', blank=True, null=True)
    headline = models.CharField(max_length=500, verbose_name='Page Headline', blank=True, null=True)
    help_tip = models.CharField(max_length=1000, verbose_name='Help tip', blank=True, null=True)
    template = models.CharField(max_length=500, verbose_name='Template path',
                                default='eat/user/application/child/earnings.html')
    next = models.ForeignKey('self', blank=True, null=True, related_name='next_page')
    skip_to = models.ForeignKey('self', blank=True, null=True, related_name='skip_page')
    display_order = models.IntegerField(verbose_name='Display Order', blank=True, null=True)

    def __str__(self):
        return '%s.%s' % (self.entity, self.name)

