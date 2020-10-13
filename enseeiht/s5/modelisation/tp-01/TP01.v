(*Modélisation TP 01*)
(*Groupe L3*)
(*PONT Sébastien ; Chaimae Ouardani ; Salahdine OUHMMIALI*)

Require Import Naturelle.
Section CalculPropositionnel.
Variable A B C E Y R : Prop.

Theorem Thm00 : A /\ B -> B /\ A.
I_imp H.
I_et.
E_et_d A.
Hyp H.
E_et_g B.
Hyp H.
Qed.

Theorem Thm_1 : ((A \/ B) -> C) -> (B -> C).
I_imp H.
I_imp J.
E_imp (A \/ B).
Hyp H.
I_ou_d.
Hyp J.
Qed.

Theorem Thm_2 : A -> ~~A.
I_imp H.
I_non J.
E_non A.
Hyp H.
Hyp J.
Qed.

Theorem Thm_3 : (A -> B) -> (~B -> ~A).
I_imp H.
I_imp J.
I_non K.
E_non B.
E_imp A.
Hyp H.
Hyp K.
Hyp J.
Qed.

Theorem Thm_4 : ~~A -> A.
I_imp H.
absurde G.
I_antiT (~A).
Hyp G.
Hyp H.
Qed.

Theorem Thm_5 : (~B -> ~A) -> (A -> B).
I_imp H.
I_imp J.
absurde K.
E_non A.
Hyp J.
E_imp (~B).
Hyp H.
Hyp K.
Qed.

Theorem Thm_6 : ((E -> (Y \/ R)) /\ (Y -> R)) -> (~R -> ~E).
I_imp H.
I_imp J.
I_non K.
I_antiT R.
E_ou Y R.
E_imp E.
E_et_g (Y -> R).
Hyp H.
Hyp K.
E_et_d (E -> Y \/ R).
Hyp H.
I_imp L.
Hyp L.
Hyp J.
Qed.


Theorem Coq_E_imp : ((A -> B) /\ A) -> B.
intro H.
destruct H as (HA,HB).
cut A.
exact HA.
exact HB.
Qed.

Theorem Coq_E_et_g : (A /\ B) -> A.
intro H.
destruct H as (HA,HB).
exact HA.
Qed.

Theorem Coq_E_ou : ((A \/ B) /\ (A -> C) /\ (B -> C)) -> C.
intro H.
destruct H as (HA,HC).
destruct HC as (HC,HD).
destruct HA as [HA | HB].
cut A.
exact HC.
exact HA.
cut B.
exact HD.
exact HB.
Qed.

Theorem Thm_7 : ((E -> (Y \/ R)) /\ (Y -> R)) -> (~R -> ~E).
unfold not.
intros F H.
destruct F as (F1,F2).
intro G.
apply H.
elim F1.
exact F2.
intro Z.
exact Z.
exact G.
Qed.

End CalculPropositionnel.