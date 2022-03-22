# https://leetcode.com/problems/unique-email-addresses/

def numUniqueEmails(emails):
        local = [e.split('@') for e in emails]

        # Split '+'
        plus = [l[0].split('+') for l in local]

        # Split and remove '.'
        period = [p[0].replace('.', '') for p in plus]

        # Put all together back
        conc = [period[i] + '@' + local[i][1] for i in range(len(emails))]

        # Remove duplicate
        return len(set(conc))