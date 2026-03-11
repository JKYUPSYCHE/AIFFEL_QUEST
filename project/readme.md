## 꽃 분류 모델 개선v2 (백본모델 비교 및 fine tuning)

<img width="849" height="541" alt="Screenshot 2026-03-11 at 4 52 45 PM" src="https://github.com/user-attachments/assets/40519d3b-6f13-4b30-9dac-74b923bcaa6f" />

<img width="848" height="536" alt="Screenshot 2026-03-11 at 5 26 35 PM" src="https://github.com/user-attachments/assets/69c522e6-417b-4dcd-8d48-34997396115d" />

### 과정
네 가지 모델(VGG16, ResNet50, MobileNetV2, EfficientNetB0)을 동일한 조건(v1 참조)으로 비교하여 가장 적합한 백본 모델 선출(winner : EfficientNetB0, 첫 번째 이미지)

### CNN layer 일부(238 레이어 중 뒤쪽 40 layers)를 unfreeze 하여 fine-tuning (classifier training: 10 epochs, fine-tuning : 10 epochs, 두 번째 이미지)
- Early CNN layers → freeze
- Middle CNN layers → freeze
- Late CNN layers → train
- Classifier head → train

### 최종 Test Accuracy : 87.5% -> 94.55%

### 회고
백본 모델간 성능 비교시, VGG16 성능에 한계가 있었음. 이는 아키텍처의 세대 차이로 인한 것(EfficientNetB0(2019), VGG16(2014))으로 보임.
fine-tuning에 의한 성능 증가가 소폭 있었음. unfreeze 할 레이어의 개수는 임의로 지정한 것이지만 적절한 숫자를 찾을 경우 정교한 fine tuning이 가능할 것으로 보임

### 의문점과 해소
fine tuning 시에 처음부터 원하는 레이어를 unfreeze 하고 학습시키는 것과, classifier 만 1차 학습 시킨 뒤 CNN layer를 unfreeze하는 것의 차이가 무엇일까?
-> classifier가 먼저 안정적으로 학습되어야 이후 fine tuning 과정에서 pretrained CNN layer feature가 훼손되지 않는다(안정성 측면).
