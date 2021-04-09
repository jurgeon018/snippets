import sys
import pytest


@pytest.fixture
def function_fixture():
   print('Fixture for each test')
   return 1


@pytest.fixture(scope='module')
def module_fixture():
   print('Fixture for module')
   return 2


@pytest.fixture
def simple_yield_fixture():
   print('setUp part')
   yield 3
   print('tearDown part')


def add(x, y=2):
      return x + y


def product(x, y=2):
    return x * y


@pytest.mark.number_mm
def test_add_strings():
      result = add('hello', 'world')
      assert result == 'helloworld'
      assert type(result) is str
      assert 'heldlo' not in result

def test_add_float():
      result = add(10.5, 25.5)
      assert result == 36


@pytest.mark.parametrize(
  'num1, num2, result',
  [
    (7, 3, 10),
    ('Hello', 'World', 'HelloWorld'),
    (10.5, 25.5, 36),
  ]
)
def test_add_with_params(num1, num2, result):
    assert add(num1, num2) == result


@pytest.mark.skipif(sys.version_info < (3.3,), reason='reason')
def test_add():
  assert add(7) == 9
  assert add(5) == 7
  assert add(7, 3) == 10
  assert add(7, 3) != 11



def test_product():
  assert product(5, 5) == 25
  assert product(7) == 14


def test_function_fixture(function_fixture):
  assert function_fixture == 1


def test_yield_fixture(simple_yield_fixture):
  assert simple_yield_fixture == 3


@pytest.mark.xfail
def test_some_magic_test():
    print('test_some_magic_test')

    
@pytest.mark.skip(reason='do nut run number add test because of ....')
def test_old_functional():
    print('test_old_functional')


@pytest.mark.parametrize(
    'text_input, result', [('5+5', 10), ('1+4', 5)]
)
def test_sum(text_input, result):
    print(text_input, result)
    print('!!!!!!!!')
    assert eval(text_input) == result



from pki_bridge.models import ProjectUser


@pytest.mark.django_db
def test_user_create():
  migrations_users = ProjectUser.objects.all().count()
  ProjectUser.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
  users = ProjectUser.objects.count()
  count =  users - migrations_users
  print(count)
  assert count == 1



from django.urls import reverse

@pytest.mark.django_db
def test_view(client):
   url = reverse('listtemplates')
   response = client.get(url)
   assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized(client):
   url = '/admin/pki_bridge/host/'
   response = client.get(url)
   assert response.status_code == 302


@pytest.mark.django_db
def test_superuser_view(admin_client):
   url = '/admin/pki_bridge/host/'
   response = admin_client.get(url)
   assert response.status_code == 200




@pytest.mark.parametrize(
  "test_input,expected", 
  [("3+5", 8), ("2+4", 6), ("6*9", 54)],
)
def test_eval(test_input, expected):
    assert eval(test_input) == expected


# fixtures


students = {
  'students': [
    {
      'id': 1,
      'name': 'Mark',
      'result': 'fail',
    },
    {
      'id': 2,
      'name': 'Scott',
      'result': 'pass',
    },
  ],
}
class StudentDb:
    
  def __init__(self):
        self.__data = None

  def close(self):
      pass
  
  def connect(self, data):
        self.__data = data

  def get_data(self, name):
    for student in self.__data['students']:
      if student['name'] == name:
        return student



def test_scott_data():
  db = StudentDb()
  db.connect(students)
  scott_data = db.get_data('Scott')
  assert scott_data['id'] == 2
  assert scott_data['name'] == 'Scott'
  assert scott_data['result'] == 'pass'


def test_mark_data():
  db = StudentDb()
  db.connect(students)
  mark_data = db.get_data('Mark')
  assert mark_data['id'] == 1
  assert mark_data['name'] == 'Mark'
  assert mark_data['result'] == 'fail'



db = None
def setup_module(module):
  print('----------setup_module-------------')
  global db
  db = StudentDb()
  db.connect(students)


def teardown_module(module):
  print('----------teardown_module-------------')
  db.close()


def test_scott_data2():
  scott_data = db.get_data('Scott')
  assert scott_data['id'] == 2
  assert scott_data['name'] == 'Scott'
  assert scott_data['result'] == 'pass'


def test_mark_data2():
  mark_data = db.get_data('Mark')
  assert mark_data['id'] == 1
  assert mark_data['name'] == 'Mark'
  assert mark_data['result'] == 'fail'


# @pytest.fixture(scope='module')
# @pytest.fixture(scope='module')
# @pytest.fixture(scope='j')
@pytest.fixture(scope='module')
def db_fixt():
  print('------------db fixture setup started------------')
  db = StudentDb()
  db.connect(students)
  # yield == setup + teardown functionality
  # return == setup functionality
  # return db
  yield db
  print('------------db fixture teardown started------------')
  db.close()


def test_scott_data3(db_fixt):
  scott_data = db.get_data('Scott')
  assert scott_data['id'] == 2
  assert scott_data['name'] == 'Scott'
  assert scott_data['result'] == 'pass'


def test_mark_data3(db_fixt):
  mark_data = db.get_data('Mark')
  assert mark_data['id'] == 1
  assert mark_data['name'] == 'Mark'
  assert mark_data['result'] == 'fail'



# @pytest.fixture(scope='function')
@pytest.fixture()
def get_driver(request):
    print('get_driver!!!!!!!!!!',)
    driver = 'driver'
    request.driver = driver
    yield
    # driver.close()


class LoginPage:
      pass

@pytest.mark.usefixtures('get_driver')
def test_login_to_jira_page_object():
  print("test_login_to_jira_page_object")
      
  # print("self: ", self)
  # self.login_page = LoginPage(self.driver)
  # self.login_page.open()


def test_pass():
      assert 1 + 1 == 2


@pytest.fixture()
def resource_setup(request):
    print("resource_setup")
    def resource_teardown():
        print("resource_teardown")
    request.addfinalizer(resource_teardown)
    
@pytest.fixture(scope="function", autouse=True)
def another_resource_setup_with_autouse(request):
    print("another_resource_setup_with_autouse")
    def resource_teardown():
        print("another_resource_teardown_with_autouse")
    request.addfinalizer(resource_teardown)
    
def test_1_that_needs_resource(resource_setup):
    print("test_1_that_needs_resource")
 

def test_2_that_does_not():
    print("test_2_that_does_not")
 

@pytest.mark.usefixtures("resource_setup")
def test_3_that_does_again():
    print("test_3_that_does_again")


def greet(person):
  return "Hi {name}".format(**person)


def test_greet():
  bob = {'name': 'bob'} # Arrange
  greeting = greet(bob) # Act
  assert greeting == 'Hi bob' # Assert



def hi(person):
  return "Hi, {name}".format(**person)

def bye(person):
  return "Bye {name}".format(**person)


def how_are_you(person):
  return "How are you {name}".format(**person)



@pytest.fixture
def bob():
    return {'name': 'Bob'}


def test_hello(bob):
    assert hi(bob) == 'Hi, Bob'


def test_bye(bob):
    assert bye(bob) == 'Bye Bob'


def test_how_are_you(bob):
    assert how_are_you(bob) == 'How are you Bob'


class Person:
      def __init__(self, name, favorite_animal=None):
            self.name = name
            self.favorite_animal = favorite_animal


def anyone_like_dogs(people):
      return any(
        p.favorite_animal == 'dog' for p in people
      )
  

@pytest.fixture
def person(**kwargs):
  count = 0
  def _person(**kwargs):
    nonlocal count
    count += 1
    name = kwargs.pop('name', f"Bob {count}")
    return Person(name=name, **kwargs)
  return _person


def test_anyone_like_dogs_true(person):
  people = [
    person(favorite_animal='cat'),
    person(favorite_animal='dog'),
  ]
  assert anyone_like_dogs(people) is True

def test_person(person):
  assert person().name != person().name
  assert person(name='alice').name == 'alice'

class TinyDB:
      def __init__(self, data):
            self.__data = data
      
      def insert(self, obj):
            self.__data.append(obj)
            
      def all(self):
            return self.__data
      
      def purge(self):
            self.__data = []

@pytest.fixture
def tiny_db():
  persons = [
    # {'name':'scott'}
  ]
  db = TinyDB(persons)
  yield db
  # return db
  db.purge()


def test_purging(tiny_db):
  assert len(tiny_db.all()) == 0


def test_inser_one(tiny_db):
  assert len(tiny_db.all()) == 0
  tiny_db.insert({'name':'bob'})
  assert len(tiny_db.all()) == 1

