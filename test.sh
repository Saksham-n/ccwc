#!/usr/bin/env bash
# ==============================================================================
# Automated Test Suite for ccwc (Comparing directly against real Unix wc)
# ==============================================================================

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

PASSED=0
FAILED=0

run_test() {
    local desc="$1"
    local cmd_ccwc="$2"
    local cmd_wc="$3"

    out_ccwc=$(eval "$cmd_ccwc" 2>&1 | tr -d '\r' | sed 's/^[ \t]*//')
    out_wc=$(eval "$cmd_wc" 2>&1 | tr -d '\r' | sed 's/^[ \t]*//')

    if [ "$out_ccwc" == "$out_wc" ]; then
        echo -e "${GREEN}[PASS]${NC} $desc"
        echo "       Got: $out_ccwc"
        ((PASSED++))
    else
        echo -e "${RED}[FAIL]${NC} $desc"
        echo "       Expected (wc):   '$out_wc'"
        echo "       Received (ccwc): '$out_ccwc'"
        ((FAILED++))
    fi
}

echo "=========================================================="
echo " Running Automated ccwc Test Suite against System wc"
echo "=========================================================="

# Step 1: Byte count
run_test "Step 1: Byte count (-c)" "python ccwc.py -c test.txt" "wc -c test.txt"

# Step 2: Line count
run_test "Step 2: Line count (-l)" "python ccwc.py -l test.txt" "wc -l test.txt"

# Step 3: Word count
run_test "Step 3: Word count (-w)" "python ccwc.py -w test.txt" "wc -w test.txt"

# Step 4: Character count
run_test "Step 4: Character count (-m)" "python ccwc.py -m test.txt" "wc -m test.txt"

# Step 5: Default (no flags)
run_test "Step 5: Default behavior (lines, words, bytes)" "python ccwc.py test.txt" "wc test.txt"

# Final Step: Standard Input
run_test "Final Step: Standard input via pipe (-l)" "cat test.txt | python ccwc.py -l" "cat test.txt | wc -l"
run_test "Final Step: Standard input default" "cat test.txt | python ccwc.py" "cat test.txt | wc"

# Extra 1: Multiple files
run_test "Extra 1: Multiple files support" "python ccwc.py -l test.txt test.txt" "wc -l test.txt test.txt"

# Extra 2: Max line length (-L)
run_test "Extra 2: Max line length (-L)" "python ccwc.py -L test.txt" "wc -L test.txt"

echo "=========================================================="
echo -e "Results: ${GREEN}$PASSED Passed${NC}, ${RED}$FAILED Failed${NC}"
echo "=========================================================="

if [ $FAILED -gt 0 ]; then
    exit 1
fi
exit 0
