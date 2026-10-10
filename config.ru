require "json"

run lambda { |env|
  body = JSON.generate(branch: "lang/ruby", lang: "ruby", path: env["PATH_INFO"])
  [200, { "content-type" => "application/json" }, [body]]
}
