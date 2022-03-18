%Dynamic Values
:- dynamic underlying_condition/1.
:- dynamic ethnicity/1.
:- dynamic patientn/9.
:- dynamic patientw/11.
:- dynamic punderlying/2.
:- dynamic psymptoms/2.
:- dynamic virusstats/5.

%Facts
virusstats(0,0,0,0,0).

%underlying_condition(['(empty)','Ash']).
underlying_condition('Diabetes').

%ethnicity(['(empty)']).
ethnicity('American').

symptoms('Fever',1).
symptoms('Cough',1).
symptoms('Tiredness',1).
symptoms('Loss of Taste',1).
symptoms('Loss of Smell',1).
symptoms('Sore throat',2).
symptoms('Headache',2).
symptoms('Aches and Pains',2).
symptoms('Diarrhoea',2).
symptoms('Skin rash or Discoloured Finers or Toes',2).
symptoms('Red or Irritated Eyes',2).
symptoms('Difficulty breathing',3).
symptoms('Shortness of Breath',3).
symptoms('Loss of speech or mobility',3).
symptoms('Confusion',3).
symptoms('Chest Pain',3).

%Rules
get_patientn(A,B,C,D,E,F,G,H,I):- patientn(A,B,C,D,E,F,G,H,I).
get_patientw(A,B,C,D,E,F,G,H,I,J,K):- patientw(A,B,C,D,E,F,G,H,I,J,K).
get_punderlying(A,B):- punderlying(A,B).
get_psymptoms(A,B):- psymptoms(A,B).

/*update_underlying_condition(Cond):- underlying_condition(Oldlist),append(Oldlist,[Cond],Newlist),
                     retractall(underlying_condition(_)),assert(underlying_condition(Newlist)).

update_ethnicity(Eth):- ethnicity(Oldlist),append(Oldlist,[Eth],Newlist),
                     retractall(ethnicity(_)),assert(ethnicity(Newlist)).

member_condition(Cond):- underlying_condition(List), member(Cond,List).
member_ethnicity(Eth):- ethnicity(List), member(Eth,List).*/




