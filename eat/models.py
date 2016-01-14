from django.db import models
from django.contrib.auth.models import User

APPLICATION_STATUSES = (
    (0, 'Start'),
    (1, 'Step 1'),
    (2, 'Complete'),
)

PAY_FREQUENCIES = (
    (0, 'Weekly'),
    (1, 'Bi-Weekly'),
    (2, '2x Month'),
    (3, 'Monthly')
)

ETHNICITIES = (
    ('Hispanic or Latino', 'Hispanic or Latino'),
    ('Not Hispanic or Latino', 'Not Hispanic or Latino'),
)

YES_NO = (
    (True, 'Yes',),
    (False, 'No',)
)

class Application(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=APPLICATION_STATUSES, verbose_name='Application Status',
                                 help_text='Application Status', default=0)
    enabled = models.BooleanField(verbose_name='Enabled', default=True)
    create_date = models.DateField(verbose_name='Create date')
    modified_date = models.DateField(verbose_name='Last modified date', blank=True, null=True)
    total_household_members = models.IntegerField(verbose_name='Total Household Members',
                                                  help_text='Total household members including children and adults',
                                                  blank=True, null=True)

    assistance_program = models.BooleanField(verbose_name='Participate in Assistance Program', choices=YES_NO, default=False)
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
    state = models.CharField(max_length=50,
                             verbose_name='State', blank=True, null=True)
    zip = models.CharField(max_length=10,
                           verbose_name='Zip', blank=True, null=True)
    phone = models.CharField(max_length=15,
                             verbose_name='Phone', blank=True, null=True)
    email = models.CharField(max_length=255,
                             verbose_name='Email', blank=True, null=True),
    ethnicity = models.CharField(max_length=25, choices=ETHNICITIES,
                                 verbose_name='Ethnicity', blank=True, null=True)
    is_american_indian = models.BooleanField(verbose_name='Is American Indian or Alaskan Native')
    is_asian = models.BooleanField(verbose_name='Is Asian')
    is_black = models.BooleanField(verbose_name='Is Black or African American')
    is_hawaiian = models.BooleanField(verbose_name='Is Hawaiian or Other Pacific Islander')
    is_white = models.BooleanField(verbose_name='Is White')


class Child(models.Model):
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
    foster_child = models.BooleanField(verbose_name='Is Foster Child')
    hmr = models.BooleanField(verbose_name='Homeless, Migrant, Runaway')
    salary = models.DecimalField(verbose_name='Salary',
                                 decimal_places=2,
                                 max_digits=8,
                                 help_text='Salary or Wages from a Job',
                                 blank=True,
                                 null=True)
    salary_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                           verbose_name='Frequency Of Salary',
                                           help_text='How often are earnings received',
                                           blank=True,
                                           null=True)
    ssi_disability = models.DecimalField(verbose_name='Social Security Income for Disabilty',
                                         decimal_places=2,
                                         max_digits=8,
                                         help_text='Social security income for childs blindness or disability',
                                         blank=True,
                                         null=True)
    ssi_disability_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                   verbose_name='Frequency Of Social Security Income for Disabilty',
                                                   help_text='How often are earnings received',
                                                   blank=True,
                                                   null=True)
    ssi_parent_disability = models.DecimalField(verbose_name='Social Security Income for Parents Disabilty',
                                                decimal_places=2,
                                                max_digits=8,
                                                help_text='Social security income received if parent is disabled/retired/deceased',
                                                blank=True,
                                                null=True)
    ssi_parent_disability_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                          verbose_name='Frequency Of Social Security Income for Parent Disabilty',
                                                          help_text='How often are earnings received',
                                                          blank=True,
                                                          null=True)
    spending_money_income = models.DecimalField(verbose_name='Spending Money Income',
                                                decimal_places=2,
                                                max_digits=8,
                                                help_text='Spending money received from a person outside the household',
                                                blank=True,
                                                null=True)
    spending_money_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                          verbose_name='Frequency Of Spending Money Income',
                                                          help_text='How often are earnings received',
                                                          blank=True,
                                                          null=True)
    other_friend_income = models.DecimalField(verbose_name='Other Regular Income From Friends',
                                              decimal_places=2,
                                              max_digits=8,
                                              blank=True,
                                              null=True)
    other_friend_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                        verbose_name='Frequency Of Other Regular Income From Friends',
                                                        help_text='How often are earnings received',
                                                        blank=True,
                                                        null=True)
    pension_income = models.DecimalField(verbose_name='Pension Income',
                                         decimal_places=2,
                                         max_digits=8,
                                         blank=True,
                                         null=True)
    pension_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                   verbose_name='Pension Income Frequency',
                                                   help_text='How often are earnings received',
                                                   blank=True,
                                                   null=True)
    annuity_income = models.DecimalField(verbose_name='Annuity Income',
                                         decimal_places=2,
                                         max_digits=8,
                                         blank=True,
                                         null=True)
    annuity_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                   verbose_name='Annuity Income Frequency',
                                                   help_text='How often are earnings received',
                                                   blank=True,
                                                   null=True)
    trust_income = models.DecimalField(verbose_name='Trust Income',
                                       decimal_places=2,
                                       max_digits=8,
                                       blank=True,
                                       null=True)
    trust_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                 verbose_name='Trust Income Frequency',
                                                 help_text='How often are earnings received',
                                                 blank=True,
                                                 null=True)
    other_income = models.DecimalField(verbose_name='Other Income',
                                       decimal_places=2,
                                       max_digits=8,
                                       help_text='Any other income',
                                       blank=True,
                                       null=True)
    other_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                 verbose_name='Other Income Frequency',
                                                 help_text='How often are earnings received',
                                                 blank=True,
                                                 null=True)


class Adult(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25,
                                  verbose_name='First Name')
    middle_name = models.CharField(max_length=25,
                                   verbose_name='Middle Name')
    last_name = models.CharField(max_length=25,
                                 verbose_name='Last Name')
    salary = models.DecimalField(verbose_name='Salary',
                                 decimal_places=2,
                                 max_digits=8,
                                 help_text='Salary from a Job',
                                 blank=True,
                                 null=True)
    salary_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                           verbose_name='Frequency Of Salary',
                                           help_text='How often are earnings received',
                                           blank=True,
                                           null=True)
    wages = models.DecimalField(verbose_name='Wages',
                                decimal_places=2,
                                max_digits=8,
                                help_text='Wages from a Job',
                                blank=True,
                                null=True)
    wages_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                          verbose_name='Frequency Of Wages',
                                          help_text='How often are earnings received',
                                          blank=True,
                                          null=True)
    cash_bonuses = models.DecimalField(verbose_name='Cash Bonuses',
                                       decimal_places=2,
                                       max_digits=8,
                                       blank=True,
                                       null=True)
    cash_bonuses_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                 verbose_name='Frequency Of Cash Bonuses',
                                                 help_text='How often are earnings received',
                                                 blank=True,
                                                 null=True)
    self_employment_income = models.DecimalField(verbose_name='Self Employment Income',
                                                 decimal_places=2,
                                                 max_digits=8,
                                                 help_text='Net income from self employment',
                                                 blank=True,
                                                 null=True)
    self_employment_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                           verbose_name='Frequency Of Self Employment Income',
                                                           help_text='How often are earnings received',
                                                           blank=True,
                                                           null=True)
    strike_benefits = models.DecimalField(verbose_name='Strike Benefits',
                                          decimal_places=2,
                                          max_digits=8,
                                          blank=True,
                                          null=True)
    strike_benefits_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                    verbose_name='Frequency Of Strike Benefits',
                                                    help_text='How often are earnings received',
                                                    blank=True,
                                                    null=True)
    unemployment_insurance = models.DecimalField(verbose_name='Unemployment Insurance',
                                                 decimal_places=2,
                                                 max_digits=8,
                                                 blank=True,
                                                 null=True)
    unemployment_insurance_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                           verbose_name='Frequency Of Unemployment Insurance',
                                                           help_text='How often are earnings received',
                                                           blank=True,
                                                           null=True)
    other_earned_income = models.DecimalField(verbose_name='Other Earned Income',
                                              decimal_places=2,
                                              max_digits=8,
                                              blank=True,
                                              null=True)
    other_earned_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                        verbose_name='Frequency Of Other Earned Income',
                                                        help_text='How often are earnings received',
                                                        blank=True,
                                                        null=True)
    military_basic_pay = models.DecimalField(verbose_name='Military Basic Pay',
                                             decimal_places=2,
                                             max_digits=8,
                                             blank=True,
                                             null=True)
    military_basic_pay_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                       verbose_name='Frequency Of Military Basic Pay',
                                                       help_text='How often are earnings received',
                                                       blank=True,
                                                       null=True)
    military_bonus = models.DecimalField(verbose_name='Military Bonus',
                                         decimal_places=2,
                                         max_digits=8,
                                         blank=True,
                                         null=True)
    military_bonus_pay_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                       verbose_name='Frequency Of Military Bonus',
                                                       help_text='How often are earnings received',
                                                       blank=True,
                                                       null=True)
    military_allowance = models.DecimalField(verbose_name='Military Allowance',
                                             decimal_places=2,
                                             max_digits=8,
                                             blank=True,
                                             null=True)
    military_allowance_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                       verbose_name='Frequency Of Military Allowance',
                                                       help_text='How often are earnings received',
                                                       blank=True,
                                                       null=True)
    military_food = models.DecimalField(verbose_name='Military Food',
                                        decimal_places=2,
                                        max_digits=8,
                                        blank=True,
                                        null=True)
    military_food_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                  verbose_name='Frequency Of Military Food',
                                                  help_text='How often are earnings received',
                                                  blank=True,
                                                  null=True)
    military_clothing = models.DecimalField(verbose_name='Military Clothing',
                                            decimal_places=2,
                                            max_digits=8,
                                            blank=True,
                                            null=True)
    military_clothing_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                      verbose_name='Frequency Of Military Clothing',
                                                      help_text='How often are earnings received',
                                                      blank=True,
                                                      null=True)
    general_assistance = models.DecimalField(verbose_name='General Assistance',
                                             decimal_places=2,
                                             max_digits=8,
                                             help_text='General assistance excluding SNAP or TANF',
                                             blank=True,
                                             null=True)
    general_assistance_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                       verbose_name='Frequency Of General Assistance',
                                                       help_text='How often are earnings received',
                                                       blank=True,
                                                       null=True)
    other_assistance = models.DecimalField(verbose_name='Other Public Assistance',
                                           decimal_places=2,
                                           max_digits=8,
                                           blank=True,
                                           null=True)
    other_assistance_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                     verbose_name='Frequency Of Other Assistance',
                                                     help_text='How often are earnings received',
                                                     blank=True,
                                                     null=True)
    alimony = models.DecimalField(verbose_name='Alimony Received',
                                  decimal_places=2,
                                  max_digits=8,
                                  blank=True,
                                  null=True)
    alimony_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                            verbose_name='Frequency Of Alimony',
                                            help_text='How often are earnings received',
                                            blank=True,
                                            null=True)
    child_support = models.DecimalField(verbose_name='Child Support',
                                        decimal_places=2,
                                        max_digits=8,
                                        blank=True,
                                        null=True)
    child_support_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                  verbose_name='Frequency Of Child Support',
                                                  help_text='How often are earnings received',
                                                  blank=True,
                                                  null=True)
    social_security_income = models.DecimalField(verbose_name='Social Security Income',
                                                 decimal_places=2,
                                                 max_digits=8,
                                                 blank=True,
                                                 null=True)
    social_security_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                           verbose_name='Frequency Of Social Security Income',
                                                           help_text='How often are earnings received',
                                                           blank=True,
                                                           null=True)
    railroad_income = models.DecimalField(verbose_name='Railroad Retirement Income',
                                          decimal_places=2,
                                          max_digits=8,
                                          blank=True,
                                          null=True)
    railroad_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                    verbose_name='Frequency Of Railroad Retirement Income',
                                                    help_text='How often are earnings received',
                                                    blank=True,
                                                    null=True)
    pension_income = models.DecimalField(verbose_name='Pension Income',
                                         decimal_places=2,
                                         max_digits=8,
                                         blank=True,
                                         null=True)
    pension_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                   verbose_name='Frequency Of Pension Income',
                                                   help_text='How often are earnings received',
                                                   blank=True,
                                                   null=True)
    annuity_income = models.DecimalField(verbose_name='Annuity Income',
                                         decimal_places=2,
                                         max_digits=8,
                                         blank=True,
                                         null=True)
    annuity_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                   verbose_name='Frequency Of Annuity Income',
                                                   help_text='How often are earnings received',
                                                   blank=True,
                                                   null=True)
    survivors_benefits = models.DecimalField(verbose_name='Survivor''s Benefits',
                                             decimal_places=2,
                                             max_digits=8,
                                             blank=True,
                                             null=True)
    survivors_benefits_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                       verbose_name='Frequency Of Survivor''s Benefits',
                                                       help_text='How often are earnings received',
                                                       blank=True,
                                                       null=True)
    ssi_disability_benefits = models.DecimalField(verbose_name='Disability Benefits From Supplemental Security Income',
                                                  decimal_places=2,
                                                  max_digits=8,
                                                  blank=True,
                                                  null=True)
    ssi_disability_benefits_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                            verbose_name='Frequency Of SSI Disability Benefits',
                                                            help_text='How often are earnings received',
                                                            blank=True,
                                                            null=True)
    private_disability_benefits = models.DecimalField(verbose_name='Private Disability Benefits',
                                                      decimal_places=2,
                                                      max_digits=8,
                                                      blank=True,
                                                      null=True)
    private_disability_benefits_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                                verbose_name='Frequency Of Private Disability Benefits',
                                                                help_text='How often are earnings received',
                                                                blank=True,
                                                                null=True)
    black_lung_benefits = models.DecimalField(verbose_name='Black Lung Benefits',
                                              decimal_places=2,
                                              max_digits=8,
                                              blank=True,
                                              null=True)
    black_lung_benefits_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                        verbose_name='Frequency Of Black Lung Benefits',
                                                        help_text='How often are earnings received',
                                                        blank=True,
                                                        null=True)
    workers_compensation = models.DecimalField(verbose_name='Worker''s Compensation',
                                               decimal_places=2,
                                               max_digits=8,
                                               blank=True,
                                               null=True)
    workers_compensation_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                         verbose_name='Frequency Of Worker''s Compensation',
                                                         help_text='How often are earnings received',
                                                         blank=True,
                                                         null=True)
    veterans_benefits = models.DecimalField(verbose_name='Veteran''s Benefits',
                                            decimal_places=2,
                                            max_digits=8,
                                            blank=True,
                                            null=True)
    veterans_benefits_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                      verbose_name='Frequency Of Veteran''s Benefits',
                                                      help_text='How often are earnings received',
                                                      blank=True,
                                                      null=True)
    other_retirement_sources = models.DecimalField(verbose_name='Other Retirement Sources',
                                                   decimal_places=2,
                                                   max_digits=8,
                                                   blank=True,
                                                   null=True)
    other_retirement_sources_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                             verbose_name='Frequency Of Other Retirement Sources',
                                                             help_text='How often are earnings received',
                                                             blank=True,
                                                             null=True)
    interest_income = models.DecimalField(verbose_name='Interest Income',
                                          decimal_places=2,
                                          max_digits=8,
                                          blank=True,
                                          null=True)
    interest_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                    verbose_name='Frequency Of Interest Income',
                                                    help_text='How often are earnings received',
                                                    blank=True,
                                                    null=True)
    dividends = models.DecimalField(verbose_name='Dividends',
                                    decimal_places=2,
                                    max_digits=8,
                                    blank=True,
                                    null=True)
    dividends_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                              verbose_name='Frequency Of Dividends',
                                              help_text='How often are earnings received',
                                              blank=True,
                                              null=True)
    trust_or_estates_income = models.DecimalField(verbose_name='Trust Or Estates Income',
                                                  decimal_places=2,
                                                  max_digits=8,
                                                  blank=True,
                                                  null=True)
    trust_or_estates_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                            verbose_name='Frequency Of Trust Or Estates Income',
                                                            help_text='How often are earnings received',
                                                            blank=True,
                                                            null=True)
    rental_income = models.DecimalField(verbose_name='Rental Income',
                                        decimal_places=2,
                                        max_digits=8,
                                        blank=True,
                                        null=True)
    rental_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                  verbose_name='Frequency Of Rental Income',
                                                  help_text='How often are earnings received',
                                                  blank=True,
                                                  null=True)
    royalties_income = models.DecimalField(verbose_name='Royalties Income',
                                           decimal_places=2,
                                           max_digits=8,
                                           blank=True,
                                           null=True)
    royalties_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                     verbose_name='Frequency Of Royalties Income',
                                                     help_text='How often are earnings received',
                                                     blank=True,
                                                     null=True)
    prize_winnings = models.DecimalField(verbose_name='Prize Winnings',
                                        decimal_places=2,
                                        max_digits=8,
                                        blank=True,
                                        null=True)
    prize_winnings_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                  verbose_name='Frequency Of Prize Winnings',
                                                  help_text='How often are earnings received',
                                                  blank=True,
                                                  null=True)
    savings_withdrawn = models.DecimalField(verbose_name='Savings Withdrawn',
                                            decimal_places=2,
                                            max_digits=8,
                                            blank=True,
                                            null=True)
    savings_withdrawn_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                      verbose_name='Frequency Of Savings Withdrawn',
                                                      help_text='How often are earnings received',
                                                      blank=True,
                                                      null=True)
    cash_gifts = models.DecimalField(verbose_name='Cash Gifts from Friends',
                                     decimal_places=2,
                                     max_digits=8,
                                     blank=True,
                                     null=True)
    cash_gifts_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                               verbose_name='Frequency Of Cash Gifts',
                                               help_text='How often are earnings received',
                                               blank=True,
                                               null=True)
