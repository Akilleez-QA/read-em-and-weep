# Reproduce the fixed P-source closure certificate

Python3 standard library only. From this directory:

    python3 verify.py > /tmp/p-source-closure.json
    cmp /tmp/p-source-closure.json RESULT.json
    python3 -O verify.py > /tmp/p-source-closure-opt.json
    cmp /tmp/p-source-closure-opt.json RESULT.json

Expected:839 explicit checks plus81 imported character-module controls. Full immutable inputs and their public URLs are authenticated in INPUTS.json. The fixed historical JSON is read and filtered, never regenerated. No actual-instance computation occurs. PROOF.md supplies the actual-map argument and specifies imported geometric prerequisites.
