# Coefficient-input conventions

Files are compact UTF-8 JSON. Rational coefficients are exact strings or integers, never floating-point approximations. Matrix triplets are `[row,column,value]`, with zero-based indices; omitted entries are zero. `*_shape` gives the complete dimensions.

The coordinate order in `B` is `0=P, 1=E0, 2=E1, 3=E2`. A symmetric slot is an ordered pair `i<=j`, representing the tensor product `Ei Ej`; the Hamiltonian convention doubles the diagonal tensor coefficient. `X,Y,W` is the ordered plane cover.

## Source and target bases

A `D` source label `[i,e,[u,v,w]]` selects the `Ai` coefficient of

```
z^e X^(-u-1)Y^(-v-1)W^(-w-1).
```

When `i=E1`, reconstruct its forced `AE0` component using the actual triangular transport: multiply by `z^-3 C`, project to all-negative plane exponents and retain the finite-regular base powers. This reconstruction is performed by `src1` in `check_early.py`; the displayed source labels are independent coordinates, not a claim of diagonal gluing.

The first four orders' `D` target labels `[[i,j],e,[p,q,r]]` use the **actual** Laurent plane exponents `p,q,r`, rather than the dual nonnegative labels. Their bases incorporate forced lower components. In extracting the order-two obstruction, the program explicitly subtracts the forced `PE0`, `E0E1`, and `E0E2` contributions before reading independent coordinates.

At orders five and six, `raw_Wk_labels` use dual nonnegative plane indices like the source labels. The complete `Ck` map imposes the remaining `E0^2` globality constraints. `Wk_kernel_free_columns` lists the independent coordinates of its kernel, which are the row-coordinate order of `Dk`. The replay recomputes the `Ck` pivots and verifies that every prescribed raw target column is a literal zero column, so no unrecorded pivot correction affects the small homogeneous block.

## Fields

- `order_1.json`: complete `D`, evaluation `Ev`, section map `N`, source/target labels, affine-origin preimage `x`, and its prescribed evaluation target `b`.
- `order_2.json`: complete `D2` and `N2`, labels and a maximal `N2` minor.
- `order_3.json`, `order_4.json`: complete `Dk`, `Nk`, labels and maximal section minors.
- `order_5.json`, `order_6.json`: complete `Dk`, `Ck`, raw target and source labels, and kernel coordinates.
- `first_jet.json`: pinned affine origin and four directions. `finite` and `infinity` entries have plane Čech degree one; `mixed` has base degree one and plane degree zero. Each term is `[symmetric_slot,[z_exp,X_exp,Y_exp,W_exp],coefficient]`; `open` lists the plane indices inverted. The complete reconstructed `nu_X` and `nu_Y` are also included.

The complete-map interpretation is an input, as explained in the main README. These files omit unrelated higher normal-jet coefficient expansions; they contain every input consumed by the advertised replay.
