%Dynamic Values
:- dynamic underlying_condition/1.
:- dynamic ethnicity/1.
:- dynamic location/1.
:- dynamic patient_info1/10.
:- dynamic patient_info2/12.
:- dynamic patient_condition/2.
:- dynamic patient_symptoms/2.
:- dynamic virusstats/6.
:- dynamic patientstats/4.
:- dynamic advice/3.

%Facts
virusstats(0,0,0,0,0,0).


underlying_condition('(empty)').

ethnicity('(empty)').

location('(empty)').

symptoms(name('Fever'), point(1)).
symptoms(name('Cough'), point(1)).
symptoms(name('Tiredness'), point(1)).
symptoms(name('Loss of Taste'), point(1)).
symptoms(name('Loss of Smell'), point(1)).
symptoms(name('Sore throat'), point(2)).
symptoms(name('Headache'), point(2)).
symptoms(name('Aches and Pains'), point(2)).
symptoms(name('Diarrhoea'), point(2)).
symptoms(name('Skin rash or Discoloured Finers or Toes'), point(2)).
symptoms(name('Red or Irritated Eyes'), point(2)).
symptoms(name('Difficulty breathing'), point(3)).
symptoms(name('Shortness of Breath'), point(3)).
symptoms(name('Loss of speech or mobility'), point(3)).
symptoms(name('Confusion'), point(3)).
symptoms(name('Chest Pain'), point(3)).

%Rules
get_patient_info1(A,B,C,D,E,F,G,H,I,J):- patient_info1(A,B,C,D,E,F,G,H,I,J).
get_patient_info2(A,B,C,D,E,F,G,H,I,J,K,L):- patient_info2(A,B,C,D,E,F,G,H,I,J,K,L).
get_patient_condition(A,B):- patient_condition(A,B).
get_patient_symptoms(A,B):- patient_symptoms(A,B).
get_patientstats(A,B,C,D):- patientstats(A,B,C,D).
get_advice(Name, B, C):- advice((patient_name(Name),moh_advice(B),patient_advice(C))).

get_condition(Cond):- underlying_condition(Cond).
get_ethnicity(Eth):- ethnicity(Eth).
get_location(Loc):- location(Loc).



