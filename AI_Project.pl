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
virusstats(mild(0), severe(0), regular(0), delta(0), omicron(0), omicronu(0)).


underlying_condition(['(empty)']).

ethnicity(['(empty)']).

location(['(empty)']).

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
get_patient_info1(A,B,C,D,E,F,G,H,I):- patient_info1(A,B,C,D,E,F,G,H,I).
get_patient_info2(A,B,C,D,E,F,G,H,I,J,K):- patient_info2(A,B,C,D,E,F,G,H,I,J,K).
get_patient_condition(A,B):- patient_condition(A,B).
get_patient_symptoms(A,B):- patient_symptoms(A,B).
get_patientstats(A,B,C,D):- patientstats(A,B,C,D).
get_advice(Name, B, C):- advice((patient_name(Name),moh_advice(B),patient_advice(C))).

update_condition(Cond,X):- underlying_condition(Oldlist),append(Oldlist,[Cond],Newlist), retractall(underlying_condition(_)),assert(underlying_condition(Newlist)),underlying_condition(X).
update_ethnicity(Eth,X):- ethnicity(Oldlist),append(Oldlist,[Eth],Newlist), retractall(ethnicity(_)),assert(ethnicity(Newlist)),ethnicity(X).
update_location(Loc,X):- location(Oldlist),append(Oldlist,[Loc],Newlist), retractall(location(_)),assert(location(Newlist)),location(X).

get_conditions(Value, List):- underlying_condition(List), member(Value, List).
get_ethnicities(Value, List):- ethnicity(List), member(Value, List).
get_locations(Value, List):- location(List), member(Value, List).
