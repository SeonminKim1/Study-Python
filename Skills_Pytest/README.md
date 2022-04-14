## Python 테스팅 기법

### Unittest vs pytest
- unittest: 파이썬 내부 테스트, Django(장고)에서 사용
- pytest: Flask(플라스크), Requests(리퀘스트), pip에서 사용
- 두 방법 다 좋으나, pytest가 좀더 많이 쓰임.

### 특징
- Unittest
    - unittest의 단점: 클래스 기반 테스트 link
    - unittest: 테스트를 작성하기 위해 반드시 클래스를 정의 필요 (불편)
    - unittest는 자바의 JUnit(J유닛) 테스팅 프레임워크로부터 영향을 받음
    - 자바는 클래스 중심적인 언어로, 클래스를 만들지 않으면 함수를 작성 불가
    - 카멜 케이스로 단어를 구분

- pytest
    - 테스트를 작성하는 데 있어 함수만 정의하면 되므로 편리합니다.
    - 기존의 여러 테스팅 프레임워크와는 다른 독특한 방식으로 픽스처를 제공
    - pytest만의 고유한 방식을 익혀야 함
    - assert 문 재작성으로 인한 편리함
    - 매개변수화된 픽스처 / 병렬 테스트 수행 가능

    
### 예제 코드 비교

``` unittest
from unittest import TestCase


class UpperTestCase(TestCase):
    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
```

``` pytest
def test_upper():
    assert "foo".upper() == "FOO"
```

### 참고문헌
- https://www.bangseongbeom.com/unittest-vs-pytest.html
- https://www.patricksoftwareblog.com/monkeypatching-with-pytest/ : monkeypatch
- https://docs.pytest.org/en/latest/reference/reference.html?highlight=monkey#monkeypatch : monkeypatch


### TEST 단계
- Arrange
    - 테스트를 위해 모든 것을 준비하는 단계
    - ex) 유저의 인증 제작, URL의 Query를 만드는 것
- Act
    - 테스트하고자 하는 Behavior 시작하는 단계, function이나 method call의 형식
- Assert
    - 결과적으로 변경된 상태를 보고 우리가 기대하는 상태와 일치하는 지를 보는 단계
- Cleanup
    - 정해진 Scope내에서 실행하고, 테스트 이후 스스로를 정리함으로서 다른 테스트에 영향이 가지 않게 하는 단계

### Pytest

- fixture
    - fixture은 환경이나 데이터셋에 대해서 테스트, "step"과 "data"을 정의하고 이 테스트를 fixture을 이용한 서비스, 상태, 조작환경등이 인자(argument)을 통해 모두 접근가능
    - 각 fixture는 보통 파라미터를 지정
    - 그리고 pytest을 이용할 때, 어떤 함수를 테스트할것인지 @pytest.fixture 와 같이 "@"데코레이터를 이용해서 설정 가능

- @pytest.mark.parametrize(ids=?)
    - parameterize로 전달해주는 파라미터에 대해서 string으로 각 아이디를 줄 수 있고, 이는 "-k"을 옵션을 이용해서 특별한 파라미터(케이스)에 대해서만 실행 가능
    
- @pytest.fixture(scope=??):
    - scope범위에 따라 데코레이터를 달아준 함수의 실행범위가 달라짐. 
    - scope="function"인 경우는 데코레이터를 달아준 함수를 매번 call해서 사용 후 소멸
    - scope="module"로 지정하면 ".py"파일 내에서는 무조건 1번만 생성
    - 한편 scope="session"인 경우는 최초 테스트 실행시 단 한번만 객체가 실행 각 테스트에서 이 하나의 객체가 호출

- Marks
    - fixtures나 plugins를 통해 접근할 수 있는 테스트 함수에 사용