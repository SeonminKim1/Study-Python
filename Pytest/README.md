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
