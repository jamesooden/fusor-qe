from selenium.webdriver.common.by import By
from pages.base import Base


class UpdateAvailability(Base):
    _page_title = "Update Availability"

    # locators
    _immediately_loc = (
        By.XPATH,
        '//div[@class = "ident-radio"]/label/input[@type = "radio" and @value="immediately"]'
    )
    _after_publishing_loc = (
        By.XPATH,
        '//div[@class = "ident-radio"]/label/input[@type = "radio" and @value="after_publishing"]'
    )
    _cancel_loc = (
        By.XPATH,
        '//button[contains(@class,"btn") and contains(., "Cancel")]'
    )
    _back_loc = (
        By.XPATH,
        '//a[contains(@class, "btn") and contains(., "Back")]',
    )
    _next_loc = (
        By.XPATH,
        '//button[contains(@class,"btn") and contains(., "Next")]'
    )

    # properties
    @property
    def immediately(self):
        return self.selenium.find_element(*self._immediately_loc)

    @property
    def after_publishing(self):
        return self.selenium.find_element(*self._after_publishing_loc)

    @property
    def cancelBtn(self):
        return self.selenium.find_element(*self._cancel_loc)

    @property
    def backBtn(self):
        return self.selenium.find_element(*self._back_loc)

    @property
    def nextBtn(self):
        return self.selenium.find_element(*self._next_loc)

    # actions
    def click_immediately(self):
        self.immediately.click()

    def click_after_publishing(self):
        self.after_publishing.click()

    def click_cancel(self):
        self.cancelBtn.click()
        # XXX: This needs some work as a second modal opens when you
        #      click this.

    def click_back(self):
        self.backBtn.click()
        return DeploymentName(self.base_url, self.selenium)

    def click_next(self):
        self.nextBtn.click()
        return Insights(self.base_url, self.selenium)

# These libraries are loaded so we can instantiate their objects after
# the navigational buttons are clicked.
# Also these libraries have to be loaded after our class is defined, because
# we have circular dependencies on one another.
from pages.wizard.satellite.deployment_name import DeploymentName
from pages.wizard.satellite.insights import Insights
