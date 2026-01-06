package io.abikussudo.sagernet.ui.profile

import io.abikussudo.sagernet.fmt.http.HttpBean

class HttpSettingsActivity : StandardV2RaySettingsActivity() {

    override fun createEntity() = HttpBean()

}
