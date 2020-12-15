def szökőév(év: int) -> bool:
    return év % 400 == 0 or év % 4 == 0 and év % 100 != 0

def main() -> None: # A N nagybetű!
    év1: int=int(input('Első évszám: '))
    év2: int=int(input('Második évszám: '))
    tól_év: int=min(év1,év2)
    ig_év: int=max(év1,év2) #beépített min/max fg
    szökőévek: List[str]=[]
    for év in range(tól_év, ig_év +1):
        if szökőév(év):
            szökőévek.append(str(év))
    
    if len(szökőévek)==0:
        print('Nincs szökőév a két évszám közt!')
    else:
        évek: str='; '.join(szökőévek)
        print(f'Szökőévek:{évek}')    


if __name__ == "__main__":
    main()