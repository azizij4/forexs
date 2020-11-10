from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from user_init.models import User

#Class for user registration
class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email',validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Register')

    #fuction for registration validation

    def validate_username(self,username):
    	user = User.query.filter_by(username=username.data).first()
    	if user:
    		raise ValidationError('That username is taken. Please choose another username')

    def validate_email(self,email):
    	user = User.query.filter_by(email=email.data).first()
    	if user:
    		raise ValidationError('That email is taken. Please choose another email')
		

#Class for user login
class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    remember = BooleanField('Remember Me')
    
    submit = SubmitField('Login')


#clss for user deposits
class Make_DepositForm(FlaskForm):
    plan  = SelectField('Plan', choices = [('A','Plan A'),('B','Plan B'),('C','Plan C')],validators=[DataRequired()])

    
    amount = SelectField('Payment', choices = [('1','15,000'),('2','25,000'),('3','35,000'),
                        ('4','45,000'),('5','55,000'),('6','65,000'),('7','75,000'),('8','85,000'),
                        ('9','95,000'),('10','100,000'),('11','115,000'),('12','125,000'),('13','135,000'),
                        ('14','145,000'),('15','155,000'),('16','165,000'),('17','175,000'),('18','185,000'),
                        ('19','195,000'),('20','200,000'),('21','255,000')],validators=[DataRequired()])


    payment = SelectField('Payment', choices = [('1','Tigo Pesa'),('2','M-Pesa'),('3','Airtel Money'),
                        ('4','T pesa'),('5','Halo pesa'),('6','CRDB bank'),('7','Bitcoin')],validators=[DataRequired()])

    payment_number = StringField('payment_number',validators=[DataRequired()])

    payment_confirmation_massege = TextAreaField('Payment_confirmation_massege',validators=[DataRequired()])

    submit =  SubmitField('Deposit')

    #function for make deposit validation
    def validate_Make_DepositForm(self,amount,plan):
        amount =  amount(amount=form.amount.data)
        Plan = plan(plan=form.plan.data)
        if Plan == "Plan A":

            plan_one_validation = ['15,000','25,000','35,000','45,000','55,000']

            for amount in plan_one_validation:

                if amount!= plan_one_validation:

                    raise ValidationError("That amount you select don't much with plan you select")

                    



      


      
                   


        



