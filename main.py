from mta import MtaClass

class MainClass:
    def main(self):
        mta = MtaClass()
        response_code = mta.get_service_status_subway()
        print(response_code)


if __name__ == '__main__':
    m = MainClass()
    m.main()