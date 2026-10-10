"""Validate precisely the character-rank fields consumed by the proof."""


def verify(report):
    expected = {'status':'PASS', 'classicalMatrixEntryIdentities':245,
                'perCharacterH1BySupportSize':[79,2,0,0,0],
                'characterMultiplicities':[1,4,6,4,1], 'totalH1':87,
                'initialRanks':[50,150,450,1250,2550],
                'weightTwoLengthThreeRank':100,
                'remainingRanks':[3598,522,90,30,10], 'trivialBoundaryRank':353}
    for key, value in expected.items():
        if report.get(key) != value:
            raise ValueError('Unexpected character rank report: '+key)
    return True
