# Healthwise-Disease_Detection_System

Introduction:
People rely heavily on the internet for medical advice, but the lack of reliable online tools results in unnecessary healthcare visits, burdening the system. This
can happen if the facility is far away or if you feel unwell at odd hours. Our website helps users detect basic non-serious diseases based on their symptoms, encouraging early
diagnosis and treatment. By providing a simple and user-friendly interface, we hope to promote healthy living and reduce the burden of preventable diseases.

Problem:
The internet's growing use for medical advice highlights the need for a dependable online tool to identify diseases based on symptoms. Without one, people may unnecessarily visit
healthcare facilities, overburden the system, and delay serious illness diagnosis and treatment.

Goal:
The goal is to create a website that detects diseases and recommends remedies based on reported symptoms. It serves as a first step for seeking medical advice, promoting early diagnosis and
treatment.

Features:
1.Disease Detection

2.First Aid and CPR Information

3.Nearby Clinics Location

4.Contact Doctor For Consultation

5.WhatsApp Bot designed to relieve stress that could occur due to panic of being diagnosed by some disease

Approach:

1 Created the dataset from various trusted websites

2. Converted the dataset into a format suitable for our application
   
3.Implementing Stratified K Fold as the dataset was imbalanced

4.Trying and evaluating various algorithms

5.Hyperparameter tuning

6.Model selection and testing on new input

Algorithms:

1.GAUSSIAN NB
Recall Score: 0.965
Accuracy Score: 0.958

2.MULTINOMIAL NB
Recall Score: 0.911
Accuracy Score: 0.949

3.DECSION TREE
Recall Score: 0.933
Accuracy Score: 0.945

4.KNN
Recall Score: 0.933
Accuracy Score: 0.953

5.Random Forest
Recall Score: 0.948
Accuracy Score: 0.957

6.Weighted KNN
Recall Score: 0.952
Accuracy Score: 0.955

Used Random Forest(Tuned) and Weighted KNN to detect diseases.

Societal Impact:

1.This project can particularly benefit underserved communities with limited access to healthcare, providing them with a valuable resource for managing
their health.

2.It can promote early diagnosis and treatment, reducing the burden on healthcare systems and improving health outcomes.

3.It can also increase health literacy with first aid and cpr guidance and help people make informed decisions about their well-being.
