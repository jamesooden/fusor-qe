from selenium.webdriver.common.by import By
from pages.qci_page import QCIPage


class InstallationReview(QCIPage):

    # locators

    _rhv_root_pw_eye_loc = (By.XPATH,
                            '//a[@data-qci="root_password_engine_&_hypervisor"]/following-sibling::i')
    _rhv_admin_pw_eye_loc = (By.XPATH,
                             '//a[@data-qci="engine_admin_password"]/following-sibling::i')
    _cfme_root_pw_eye_loc = (By.XPATH,
                             '//a[@data-qci="cfme_root_password"]/following-sibling::i')
    _cfme_admin_pw_eye_loc = (By.XPATH,
                              '//a[@data-qci="cfme_admin_password"]/following-sibling::i')
    _cfme_database_pw_eye_loc = (By.XPATH,
                                 '//a[@data-qci="cfme_database_password"]/following-sibling::i')
    _deploy_button_loc = (By.XPATH,
                          '//button[text()="Deploy"]')
    _build_task_spinner_locator = (
        By.XPATH,
        "//div[contains(@class, 'spinner-md')]")

    _build_task_spinner_locator_text = (
        By.XPATH,
        "//span[contains(@class, 'spinner-text') and contains(., 'Building task list']")

    # elements
    @property
    def rhv_root_pw_eye_icon(self):
        return self.selenium.find_element(*self._rhv_root_pw_eye_loc)

    @property
    def rhv_admin_pw_eye_icon(self):
        return self.selenium.find_element(*self._rhv_admin_pw_eye_loc)

    @property
    def cfme_admin_pw_eye_icon(self):
        return self.selenium.find_element(*self._cfme_admin_pw_eye_loc)

    @property
    def cfme_root_pw_eye_icon(self):
        return self.selenium.find_element(*self._cfme_root_pw_eye_loc)

    @property
    def cfme_database_pw_eye_icon(self):
        return self.selenium.find_element(*self._cfme_database_pw_eye_loc)

    @property
    def deploy_button(self):
        return self.selenium.find_element(*self._deploy_button_loc)

    @property
    def building_task_spinner(self):
        return self.selenium.find_element(*self._build_task_spinner_locator)

    @property
    def building_task_spinner_text(self):
        return self.selenium.find_element(*self._build_task_spinner_locator_text)

    # actions

    def reveal_rhv_root_pw(self):
        return self.rhv_root_pw_eye_icon.click()

    def reveal_rhv_admin_pw(self):
        return self.rhv_admin_pw_eye_icon.click()

    def reveal_cfme_admin_pw(self):
        return self.cfme_admin_pw_eye_icon.click()

    def reveal_cfme_root_pw(self):
        return self.cfme_root_pw_eye_icon.click()

    def reveal_cfme_database_pw(self):
        return self.cfme_database_pw_eye_icon.click()

    def click_deploy(self):
        from pages.wizard.review.installation_progress import InstallationProgress
        self.wait_for_ajax()
        self.deploy_button.click()
        self.wait_until_element_is_not_visible(self._build_task_spinner_locator, timeout=120)
        return InstallationProgress(self.base_url, self.selenium)
