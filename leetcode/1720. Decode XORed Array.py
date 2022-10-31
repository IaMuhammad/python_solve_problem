def decode(encoded, first):
    answer = [first]

    for indx in range(0, len(encoded)):
        answer.append(encoded[indx] ^ answer[indx])
        print()

    return answer

a = [1, 2, 3]
print(decode(a, 1))