import random

prepositions_all = ['angry about/at/with',
                    'anxious about',
                    'enthusiastic about',
                    'excited about/at/by',
                    'furious about/with',
                    'happy about',
                    'mad about/at',
                    'nervous about',
                    'pessimistic about',
                    'sad about',
                    'serious about',
                    'upset about',
                    'worried about',
                    'amazed at/by',
                    'annoyed at',
                    'awful at',
                    'bad at',
                    'brilliant at',
                    'clever at',
                    'delighted at/by/with',
                    'disappointed at/in/with',
                    'excellent at',
                    'good at',
                    'hopeless at',
                    'present at/in',
                    'shocked at/by',
                    'skilled at/in',
                    'successful at/in',
                    'surprised at/by',
                    'terrible at',
                    'slow at/in',
                    'lucky at ',
                    'disturbed by',
                    'fascinated by',
                    'impressed by',
                    'inspired by',
                    'astonished by',
                    'eager for',
                    'eligible for',
                    'famous for',
                    'grateful for',
                    'notorious for',
                    'prepared for',
                    'ready for',
                    'renowned for',
                    'responsible for',
                    'respected for',
                    'sorry for',
                    'suitable for',
                    'thankful for',
                    'experienced in',
                    'interested in',
                    'involved in',
                    'polite in',
                    'impolite in',
                    'talented in ',
                    'afraid of',
                    'ashamed of',
                    'aware of',
                    'capable of',
                    'certain of',
                    'conscious of',
                    'envious of',
                    'independent of',
                    'jealous of',
                    'kind of/to',
                    'nice of',
                    'proud of',
                    'scared of',
                    'silly of',
                    'sweet of',
                    'typical of',
                    'accustomed to',
                    'addicted to',
                    'allergic to',
                    'committed to',
                    'dedicated to',
                    'indifferent to',
                    'married to',
                    'opposed to',
                    'receptive to',
                    'related to',
                    'similar to',
                    'superior to',
                    'unfriendly to',
                    'associated with',
                    'bored with',
                    'blessed with',
                    'confronted with',
                    'content with',
                    'crowded with',
                    'fed up with',
                    'familiar with',
                    'ok with',
                    'pleased with',
                    'popular with',
                    'satisfied with']


def game(prepositions_all):
    print('For each adjective give the appropriate preposition \nPS: If there are more than one preposition give one \n -- Enter \'done\' to finish the game --\n')
    i = 0  # number of total answers
    j = 0  # number of correct answers
    prepositions = list(prepositions_all)
    while i < len(prepositions_all):
        i += 1
        exp = random.choice(prepositions)
        prepositions.remove(exp)
        adj = exp.split()[0]
        cor_ans = exp.split()[1]
        ans = input(f'{i}-{adj} ')
        if 'done' in ans.lower():
            print(f' \n Your score: \n {j} out of {i-1}')
            if i-1 == 0:
                pass
            elif j == 0 and i-1 != 0:
                print(' Oops you should revise you lessons')
            elif j/(i-1) >= 10/20:
                print(' Good')
            elif j/(i-1) >= 15/20:
                print(' Excellent')
            else:
                print('You can do better')

            break

        elif ans.lower() in cor_ans.split('/'):
            j += 1
            print(f'Correct! {adj} {cor_ans} \n' if len(
                cor_ans.split('/')) > 1 else 'Correct!\n')
        else:
            print(f'Wrong answer! {adj} {cor_ans} \n')


if __name__ == '__main__':
    game(prepositions_all)
