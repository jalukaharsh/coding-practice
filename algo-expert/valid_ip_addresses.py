

def validate(candidate: str) -> list:
    """Generate all possible IP addresses given a string of numbers. Return empty list if no possible IP addresses can
    be generated.

    O(1) time and O(1) space complexity

    :param candidate: string of integers
    :return: list of valid IP addresses
    """
    if len(candidate) < 4 or len(candidate) > 12:
        return []

    valid_lst = []

    for i in range(1, 4):
        for j in range(i+1, i+4):
            for k in range(j+1, j+4):
                first = candidate[:i]
                second = candidate[i:j]
                third = candidate[j:k]
                fourth = candidate[k:]
                potential_ip = [first, second, third, fourth]
                if '' not in potential_ip:
                    if is_valid(first) and is_valid(second) and is_valid(third) and is_valid(fourth):
                        valid_ip = '.'.join(potential_ip)
                        valid_lst.append(valid_ip)

    return valid_lst


def is_valid(substr: str):
    int_substr = int(substr)
    if int_substr > 255:
        return False

    return len(str(int_substr)) == len(substr)


if __name__ == '__main__':
    validated_ips = validate('1921680')
    print(validated_ips)
    print(len(validated_ips))