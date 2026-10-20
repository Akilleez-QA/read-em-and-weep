(vrml-ir 1
  (function (id "bounded" () "residue_term")
    (typarams)
    (binders ("e0" Int) ("e1" Int) ("e2" Int) ("e3" Int) ("e4" Int) ("coefficient" Int))
    (requires (srange 64 (var "e0")) (srange 64 (var "e1")) (srange 64 (var "e2")) (srange 64 (var "e3")) (srange 64 (var "e4")) (srange 64 (var "coefficient")))
    (body
      (assert (clause "0" (span "examples/bounded-residue/bounded.rs" 12 14 12 16) (srange 64 (sub (int 0) (int 1))) "possible arithmetic underflow/overflow"))
      (fresh ("tmp_" Prop))
      (branch (eq (var "e0") (sclip 64 (sub (int 0) (int 1))))
        (then
          (assert (clause "1" (span "examples/bounded-residue/bounded.rs" 12 26 12 28) (srange 64 (sub (int 0) (int 1))) "possible arithmetic underflow/overflow"))
          (assume (iff (var "tmp_") (eq (var "e1") (sclip 64 (sub (int 0) (int 1))))))
        )
        (else
          (assume (iff (var "tmp_") false))
        ))
      (fresh ("tmp__2" Prop))
      (branch (var "tmp_")
        (then
          (assert (clause "2" (span "examples/bounded-residue/bounded.rs" 12 38 12 40) (srange 64 (sub (int 0) (int 1))) "possible arithmetic underflow/overflow"))
          (assume (iff (var "tmp__2") (eq (var "e2") (sclip 64 (sub (int 0) (int 1))))))
        )
        (else
          (assume (iff (var "tmp__2") false))
        ))
      (fresh ("tmp__3" Prop))
      (branch (var "tmp__2")
        (then
          (assert (clause "3" (span "examples/bounded-residue/bounded.rs" 12 50 12 52) (srange 64 (sub (int 0) (int 1))) "possible arithmetic underflow/overflow"))
          (assume (iff (var "tmp__3") (eq (var "e3") (sclip 64 (sub (int 0) (int 1))))))
        )
        (else
          (assume (iff (var "tmp__3") false))
        ))
      (fresh ("tmp__4" Prop))
      (branch (var "tmp__3")
        (then
          (assert (clause "4" (span "examples/bounded-residue/bounded.rs" 12 62 12 64) (srange 64 (sub (int 0) (int 1))) "possible arithmetic underflow/overflow"))
          (assume (iff (var "tmp__4") (eq (var "e4") (sclip 64 (sub (int 0) (int 1))))))
        )
        (else
          (assume (iff (var "tmp__4") false))
        ))
      (ensures (clause "5" (span "examples/bounded-residue/bounded.rs" 8 13 10 18) (eq (ite (var "tmp__4") (var "coefficient") (int 0)) (ite (and (and (and (and (eq (var "e0") (sub (int 0) (int 1))) (eq (var "e1") (sub (int 0) (int 1)))) (eq (var "e2") (sub (int 0) (int 1)))) (eq (var "e3") (sub (int 0) (int 1)))) (eq (var "e4") (sub (int 0) (int 1)))) (var "coefficient") (int 0))) "function postcondition (`ensures`)"))
    ))
  (function (id "bounded" () "residue_two")
    (typarams)
    (binders ("a0" Int) ("a1" Int) ("a2" Int) ("a3" Int) ("a4" Int) ("ca" Int) ("b0" Int) ("b1" Int) ("b2" Int) ("b3" Int) ("b4" Int) ("cb" Int))
    (requires (srange 64 (var "a0")) (srange 64 (var "a1")) (srange 64 (var "a2")) (srange 64 (var "a3")) (srange 64 (var "a4")) (srange 64 (var "ca")) (srange 64 (var "b0")) (srange 64 (var "b1")) (srange 64 (var "b2")) (srange 64 (var "b3")) (srange 64 (var "b4")) (srange 64 (var "cb")) (and (le (sub (int 0) (int 4611686018427387903)) (var "ca")) (le (var "ca") (int 4611686018427387903))) (and (le (sub (int 0) (int 4611686018427387903)) (var "cb")) (le (var "cb") (int 4611686018427387903))))
    (body
      (assume (srange 64 (ite (and (and (and (and (eq (var "a0") (sub (int 0) (int 1))) (eq (var "a1") (sub (int 0) (int 1)))) (eq (var "a2") (sub (int 0) (int 1)))) (eq (var "a3") (sub (int 0) (int 1)))) (eq (var "a4") (sub (int 0) (int 1)))) (var "ca") (int 0))))
      (assume (srange 64 (ite (and (and (and (and (eq (var "b0") (sub (int 0) (int 1))) (eq (var "b1") (sub (int 0) (int 1)))) (eq (var "b2") (sub (int 0) (int 1)))) (eq (var "b3") (sub (int 0) (int 1)))) (eq (var "b4") (sub (int 0) (int 1)))) (var "cb") (int 0))))
      (assert (clause "2" (span "examples/bounded-residue/bounded.rs" 26 5 26 10) (srange 64 (add (ite (and (and (and (and (eq (var "a0") (sub (int 0) (int 1))) (eq (var "a1") (sub (int 0) (int 1)))) (eq (var "a2") (sub (int 0) (int 1)))) (eq (var "a3") (sub (int 0) (int 1)))) (eq (var "a4") (sub (int 0) (int 1)))) (var "ca") (int 0)) (ite (and (and (and (and (eq (var "b0") (sub (int 0) (int 1))) (eq (var "b1") (sub (int 0) (int 1)))) (eq (var "b2") (sub (int 0) (int 1)))) (eq (var "b3") (sub (int 0) (int 1)))) (eq (var "b4") (sub (int 0) (int 1)))) (var "cb") (int 0)))) "possible arithmetic underflow/overflow"))
      (ensures (clause "3" (span "examples/bounded-residue/bounded.rs" 21 13 22 97) (eq (sclip 64 (add (ite (and (and (and (and (eq (var "a0") (sub (int 0) (int 1))) (eq (var "a1") (sub (int 0) (int 1)))) (eq (var "a2") (sub (int 0) (int 1)))) (eq (var "a3") (sub (int 0) (int 1)))) (eq (var "a4") (sub (int 0) (int 1)))) (var "ca") (int 0)) (ite (and (and (and (and (eq (var "b0") (sub (int 0) (int 1))) (eq (var "b1") (sub (int 0) (int 1)))) (eq (var "b2") (sub (int 0) (int 1)))) (eq (var "b3") (sub (int 0) (int 1)))) (eq (var "b4") (sub (int 0) (int 1)))) (var "cb") (int 0)))) (add (ite (and (and (and (and (eq (var "a0") (sub (int 0) (int 1))) (eq (var "a1") (sub (int 0) (int 1)))) (eq (var "a2") (sub (int 0) (int 1)))) (eq (var "a3") (sub (int 0) (int 1)))) (eq (var "a4") (sub (int 0) (int 1)))) (var "ca") (int 0)) (ite (and (and (and (and (eq (var "b0") (sub (int 0) (int 1))) (eq (var "b1") (sub (int 0) (int 1)))) (eq (var "b2") (sub (int 0) (int 1)))) (eq (var "b3") (sub (int 0) (int 1)))) (eq (var "b4") (sub (int 0) (int 1)))) (var "cb") (int 0)))) "function postcondition (`ensures`)"))
    ))
)
