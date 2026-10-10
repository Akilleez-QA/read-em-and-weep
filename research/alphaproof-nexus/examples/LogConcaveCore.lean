/-
Copyright 2026 Google LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-/

import Mathlib

-- Imported proof body unchanged; placed in a local namespace.
namespace AlphaProofNexusExample

lemma log_concave_core (x y z : ℤ) (hx : x ≥ 0) (hz : z ≤ 2) (hy : z = 1 → y^2 ≥ x) (hy2 : z = 2 → y^2 ≥ 2*x) :
  y^2 ≥ x * z := by
  have h_cases : z ≤ 0 ∨ z = 1 ∨ z = 2 := by omega
  rcases h_cases with h0 | h1 | h2
  · have h1 : x * z ≤ 0 := mul_nonpos_of_nonneg_of_nonpos hx h0
    have h2 : 0 ≤ y^2 := sq_nonneg y
    omega
  · rw [h1]
    have h3 : y^2 ≥ x := hy h1
    omega
  · rw [h2]
    have h3 : y^2 ≥ 2*x := hy2 h2
    omega

end AlphaProofNexusExample
