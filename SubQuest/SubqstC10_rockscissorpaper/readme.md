# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 유진국
- 리뷰어 : 손정희


# PRT(Peer Review Template)
- [ ]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - 문제에서 요구하는 최종 결과물이 첨부되었는지 확인하였습니다. 
        - 해당 조건을 만족하는 부분을 캡쳐해 근거로 첨부 --> 하단에 관련 코드 부분 추가함
        - ```
          test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=2)
          print("test_loss: {} ".format(test_loss))
          print("test_accuracy: {}".format(test_accuracy))

          11/11 - 0s - loss: 2.2353 - accuracy: 0.3155
          test_loss: 2.2352874279022217
          test_accuracy: 0.3154761791229248
          ```
    
- [ ]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - 전반적으로 코드가 간결해서 이해하기 쉬웠습니다. 
        - 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부  --> 하단에 관련 코드 부분 추가함
        - ```
          import tensorflow as tf
          from tensorflow import keras
          import numpy as np
          # model을 직접 만들어 보세요.
          # Hint! model의 입력/출력부에 특히 유의해 주세요. 가위바위보 데이터셋은 MNIST 데이터셋과 어떤 점이 달라졌나요?
          n_channel_1= 32
          n_channel_2= 64
          n_dense= 64
          n_train_epoch= 60

          model=keras.models.Sequential()
          model.add(keras.layers.Conv2D(n_channel_1, (3,3), activation='relu', input_shape=(28,28,3)))
          model.add(keras.layers.MaxPool2D(2,2))
          model.add(keras.layers.Conv2D(n_channel_2, (3,3), activation='relu'))
          model.add(keras.layers.MaxPooling2D((2,2)))
          model.add(keras.layers.Flatten())
          model.add(keras.layers.Dense(n_dense, activation='relu'))
          model.add(keras.layers.Dense(3, activation='softmax'))

          model.summary()
          ```
        
- [ ]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**
    - 별도로 에러가 난 부분은 확인할 수 없었습니다. 
        
- [ ]  **4. 회고를 잘 작성했나요?**
    - 실험 결과가 코드에 반영되어 있어서 내용을 확인하였습니다. 
        
- [ ]  **5. 코드가 간결하고 효율적인가요?**
    - 코드중복을 확인할 수 없었고 내용이 간결하여 이해해 어려움이 없었습니다. 

# 회고(참고 링크 및 코드 개선)
```
# 해당없음
```
